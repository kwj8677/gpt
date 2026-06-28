from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.parse import quote_plus, urlparse
import csv
import json
import re
import time
import urllib.error
import urllib.request


@dataclass(frozen=True)
class Target:
    """A target site or URL pattern to find in search results."""

    name: str
    patterns: tuple[str, ...]

    def matches(self, url: str) -> bool:
        normalized_url = normalize_url(url)
        host = urlparse(normalized_url).netloc.lower()
        for pattern in self.patterns:
            normalized_pattern = pattern.strip().lower()
            if not normalized_pattern:
                continue
            if "://" in normalized_pattern:
                if normalized_url.startswith(normalize_url(normalized_pattern)):
                    return True
            elif normalized_pattern in host or normalized_pattern in normalized_url:
                return True
        return False


@dataclass(frozen=True)
class RankMatch:
    rank: int
    title: str
    url: str


@dataclass(frozen=True)
class RankResult:
    checked_at: str
    keyword: str
    target: str
    best_rank: int | None
    matches: tuple[RankMatch, ...]
    total_results_checked: int

    @property
    def status(self) -> str:
        return "found" if self.best_rank is not None else "not_found"


class SearchRankingTracker:
    """Track target-site rankings for keywords using a pluggable search endpoint."""

    def __init__(
        self,
        targets: Iterable[Target],
        *,
        engine_url: str = "https://duckduckgo.com/html/?q={query}",
        user_agent: str = "Mozilla/5.0 rank-tracker/1.0",
        timeout_seconds: int = 20,
        delay_seconds: float = 1.0,
    ) -> None:
        self.targets = tuple(targets)
        self.engine_url = engine_url
        self.user_agent = user_agent
        self.timeout_seconds = timeout_seconds
        self.delay_seconds = delay_seconds

    def track(self, keywords: Iterable[str], *, limit: int = 30) -> list[RankResult]:
        results: list[RankResult] = []
        for keyword in keywords:
            html = self.fetch(keyword)
            organic_results = parse_search_results(html)[:limit]
            checked_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
            for target in self.targets:
                matches = tuple(
                    RankMatch(rank=index, title=title, url=url)
                    for index, (title, url) in enumerate(organic_results, start=1)
                    if target.matches(url)
                )
                results.append(
                    RankResult(
                        checked_at=checked_at,
                        keyword=keyword,
                        target=target.name,
                        best_rank=matches[0].rank if matches else None,
                        matches=matches,
                        total_results_checked=len(organic_results),
                    )
                )
            time.sleep(self.delay_seconds)
        return results

    def fetch(self, keyword: str) -> str:
        url = self.engine_url.format(query=quote_plus(keyword))
        request = urllib.request.Request(url, headers={"User-Agent": self.user_agent})
        try:
            with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                return response.read().decode("utf-8", errors="replace")
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Search request failed for '{keyword}': {exc}") from exc


def normalize_url(url: str) -> str:
    parsed = urlparse(url.strip())
    if not parsed.scheme:
        parsed = urlparse("https://" + url.strip())
    host = parsed.netloc.lower().removeprefix("www.")
    path = re.sub(r"/+$", "", parsed.path)
    return parsed._replace(netloc=host, path=path).geturl().lower()


class AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._current_href: str | None = None
        self._current_text: list[str] = []
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "a":
            href = dict(attrs).get("href")
            if href:
                self._current_href = href
                self._current_text = []

    def handle_data(self, data: str) -> None:
        if self._current_href is not None:
            self._current_text.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self._current_href is not None:
            title = " ".join("".join(self._current_text).split())
            if title:
                self.links.append((title, self._current_href))
            self._current_href = None
            self._current_text = []


def parse_search_results(html: str) -> list[tuple[str, str]]:
    parser = AnchorParser()
    parser.feed(html)
    seen: set[str] = set()
    results: list[tuple[str, str]] = []
    for title, href in parser.links:
        url = extract_result_url(href)
        if not url or is_search_chrome(url):
            continue
        normalized = normalize_url(url)
        if normalized in seen:
            continue
        seen.add(normalized)
        results.append((title, url))
    return results


def extract_result_url(href: str) -> str | None:
    if href.startswith("//duckduckgo.com/l/?") or href.startswith("https://duckduckgo.com/l/?"):
        query = urlparse(href).query
        for part in query.split("&"):
            if part.startswith("uddg="):
                from urllib.parse import unquote

                return unquote(part[5:])
    if href.startswith("http://") or href.startswith("https://"):
        return href
    return None


def is_search_chrome(url: str) -> bool:
    host = urlparse(url).netloc.lower()
    blocked_hosts = ("duckduckgo.com", "google.com", "bing.com", "yahoo.com")
    return any(host == blocked or host.endswith("." + blocked) for blocked in blocked_hosts)


def load_config(path: str | Path) -> tuple[list[str], list[Target]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    keywords = [str(keyword) for keyword in data.get("keywords", [])]
    targets = [
        Target(name=str(item["name"]), patterns=tuple(str(pattern) for pattern in item["patterns"]))
        for item in data.get("targets", [])
    ]
    if not keywords:
        raise ValueError("config must contain at least one keyword")
    if not targets:
        raise ValueError("config must contain at least one target")
    return keywords, targets


def write_csv(path: str | Path, results: Iterable[RankResult]) -> None:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    file_exists = output.exists()
    with output.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=["checked_at", "keyword", "target", "status", "best_rank", "matched_url", "total_results_checked"],
        )
        if not file_exists:
            writer.writeheader()
        for result in results:
            writer.writerow(
                {
                    "checked_at": result.checked_at,
                    "keyword": result.keyword,
                    "target": result.target,
                    "status": result.status,
                    "best_rank": result.best_rank or "",
                    "matched_url": result.matches[0].url if result.matches else "",
                    "total_results_checked": result.total_results_checked,
                }
            )
