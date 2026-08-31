from __future__ import annotations

import html
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "magazine"
OUT = ROOT / "docs" / "magazine"
ASSETS = OUT / "assets"

ISSUES = [
    ("01", "01-pickpocket-deterrence.ko.md", "지갑을 노리는 사업이 망하는 법", "도시·범죄", "출처 기반 분석"),
    ("02", "02-objective-lock.ko.md", "대화가 길어질수록 목표는 어디로 사라지는가", "AI·에이전트", "가설 에세이 / 평가 설계"),
    ("03", "03-imax-1570-vs-digital.ko.md", "‘18K’라는 숫자 밖의 IMAX", "영상·기술", "기술 해설"),
    ("04", "04-bitcoin-exit-liquidity-2026-08.ko.md", "8만 달러의 환승역", "시장·경제", "시점 명시 분석"),
    ("05", "05-fusion-commercialization-bottlenecks.ko.md", "1억 도 다음에 오는 것", "에너지·공학", "출처 기반 분석"),
    ("06", "06-hunminjeongeum-voice-notation.ko.md", "목소리를 위한 두 번째 악보", "언어·AI", "인터페이스 가설"),
    ("07", "07-structural-cutting.ko.md", "머리는 선이 아니라 무게로 움직인다", "헤어·디자인", "실무 기반 에세이"),
]

CSS = r'''@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700&family=Noto+Serif+KR:wght@400;500;600;700&display=swap');

:root {
  --paper: #f4f1e8;
  --paper-2: #fbf9f3;
  --ink: #1a1916;
  --muted: #69655d;
  --faint: #9b9589;
  --rule: #cfc9bc;
  --rule-dark: #8d877d;
  --accent: #304e5c;
  --accent-2: #704f3b;
  --serif: 'Noto Serif KR', 'Nanum Myeongjo', 'AppleMyungjo', 'Batang', serif;
  --sans: 'Noto Sans KR', 'Pretendard', 'Apple SD Gothic Neo', 'Malgun Gothic', sans-serif;
  --measure: 42rem;
  --step--1: .78rem;
  --step-0: 1rem;
  --step-1: 1.18rem;
  --step-2: 1.48rem;
  --step-3: 1.92rem;
  --step-4: 2.62rem;
  --step-5: 3.65rem;
}

* { box-sizing: border-box; }
html { color-scheme: light; background: var(--paper); font-kerning: normal; text-rendering: optimizeLegibility; }
body {
  margin: 0;
  color: var(--ink);
  background: var(--paper);
  font-family: var(--serif);
  font-size: 18px;
  line-height: 1.92;
  word-break: keep-all;
  overflow-wrap: break-word;
  font-feature-settings: 'kern' 1, 'palt' 1;
}
a { color: inherit; text-decoration-color: #80786d; text-underline-offset: .18em; text-decoration-thickness: .06em; }
a:hover { color: var(--accent); text-decoration-color: currentColor; }
::selection { background: #d7dfdc; }

.masthead {
  height: 66px;
  border-bottom: 1px solid var(--rule-dark);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.5rem;
  padding: 0 4vw;
  font: 600 .72rem/1 var(--sans);
  letter-spacing: .13em;
  text-transform: uppercase;
  font-variant-numeric: tabular-nums;
}
.masthead a { text-decoration: none; }
.masthead .edition { color: var(--muted); font-weight: 500; }

.page { width: min(1180px, 92vw); margin: 0 auto; }
.article-header { padding: clamp(4.5rem, 10vw, 8rem) 0 3.5rem; border-bottom: 1px solid var(--rule-dark); }
.kicker { font: 600 .72rem/1.4 var(--sans); letter-spacing: .14em; text-transform: uppercase; color: var(--accent); margin-bottom: 1.35rem; }
h1.article-title {
  max-width: 17ch;
  margin: 0;
  font-family: var(--serif);
  font-size: clamp(2.65rem, 6vw, var(--step-5));
  line-height: 1.16;
  letter-spacing: -.055em;
  font-weight: 700;
  text-wrap: balance;
}
.deck { margin: 1.6rem 0 0; max-width: 50rem; color: #3e3b36; font-size: 1.14rem; line-height: 1.75; }
.article-meta { margin-top: 2.4rem; display: flex; gap: .9rem 1.5rem; flex-wrap: wrap; color: var(--muted); font: 500 .76rem/1.5 var(--sans); letter-spacing: .02em; font-variant-numeric: tabular-nums; }
.article-meta span + span::before { content: '·'; margin-right: 1.5rem; color: var(--faint); }

.article-grid { display: grid; grid-template-columns: minmax(0, var(--measure)) minmax(180px, 1fr); gap: clamp(3rem, 8vw, 7.5rem); align-items: start; padding: 4.4rem 0 7rem; }
.article-body { width: 100%; min-width: 0; }
.article-body > :first-child { margin-top: 0; }
.article-body p { margin: 0 0 1.35em; orphans: 3; widows: 3; }
.article-body h2 { margin: 3.7rem 0 1.25rem; padding-top: .8rem; border-top: 1px solid var(--rule); font: 700 var(--step-3)/1.35 var(--serif); letter-spacing: -.035em; text-wrap: balance; }
.article-body h3 { margin: 2.7rem 0 1rem; font: 700 var(--step-2)/1.4 var(--serif); letter-spacing: -.025em; }
.article-body strong { font-weight: 700; }
.article-body em { font-style: normal; text-decoration: underline; text-decoration-thickness: .05em; text-underline-offset: .15em; }
.article-body code { font-family: ui-monospace, SFMono-Regular, Consolas, monospace; font-size: .83em; background: #e9e5dc; padding: .12em .34em; border-radius: 2px; word-break: break-all; }
.article-body pre { margin: 2rem 0; padding: 1.25rem 1.35rem; overflow-x: auto; background: #e7e2d8; border-top: 1px solid var(--rule-dark); border-bottom: 1px solid var(--rule-dark); font: .82rem/1.7 ui-monospace, SFMono-Regular, Consolas, monospace; }
.article-body pre code { padding: 0; background: transparent; }
.article-body ul, .article-body ol { margin: 1.1rem 0 1.8rem; padding-left: 1.35rem; }
.article-body li { margin: .35rem 0; padding-left: .2rem; }
.article-body hr { border: 0; border-top: 1px solid var(--rule-dark); margin: 3.6rem 0; }

.evidence-note { margin: 0 0 3rem; padding: 1.2rem 1.25rem 1.25rem; border: 1px solid var(--rule-dark); border-left: 4px solid var(--accent); background: var(--paper-2); font: .86rem/1.75 var(--sans); color: #3f3b35; }
.pullquote { margin: 2.8rem -.5rem 3rem; padding: 1.6rem .5rem 1.5rem; border-top: 2px solid var(--ink); border-bottom: 1px solid var(--rule-dark); font: 600 clamp(1.35rem, 3vw, 1.8rem)/1.62 var(--serif); letter-spacing: -.028em; }
.pullquote p { margin: 0; }

.figure { margin: 2.5rem 0 3.2rem; }
.figure img { width: 100%; height: auto; display: block; border: 1px solid var(--rule); background: #fbfaf7; }
.figure figcaption { margin-top: .75rem; color: var(--muted); font: .72rem/1.6 var(--sans); }

.table-wrap { overflow-x: auto; margin: 2rem 0 3rem; border-top: 2px solid var(--ink); border-bottom: 1px solid var(--rule-dark); }
table { border-collapse: collapse; width: 100%; min-width: 560px; font: .76rem/1.62 var(--sans); font-variant-numeric: tabular-nums; }
th, td { padding: .8rem .72rem; text-align: left; vertical-align: top; border-bottom: 1px solid var(--rule); }
th { font-weight: 700; background: rgba(255,255,255,.25); }
tbody tr:last-child td { border-bottom: 0; }
td:nth-child(n+2), th:nth-child(n+2) { font-variant-numeric: tabular-nums; }

.margin-note { position: sticky; top: 2rem; color: var(--muted); font: .72rem/1.72 var(--sans); border-top: 1px solid var(--rule-dark); padding-top: .9rem; }
.margin-note strong { color: var(--ink); display: block; margin-bottom: .55rem; font-weight: 700; }
.margin-note .folio { display: inline-block; margin-bottom: 1.2rem; font-size: 1.7rem; line-height: 1; color: var(--faint); font-weight: 500; letter-spacing: -.04em; font-variant-numeric: tabular-nums; }

.issue-nav { border-top: 1px solid var(--rule-dark); border-bottom: 1px solid var(--rule-dark); display: grid; grid-template-columns: 1fr 1fr; margin-top: 4rem; }
.issue-nav a { padding: 1.2rem 0; font: .76rem/1.5 var(--sans); text-decoration: none; }
.issue-nav a:last-child { text-align: right; }

.index-hero { padding: clamp(4.5rem, 10vw, 7.5rem) 0 4rem; border-bottom: 1px solid var(--rule-dark); }
.index-hero h1 { margin: 0; max-width: 13ch; font: 700 clamp(3rem, 8vw, 5.6rem)/1.04 var(--serif); letter-spacing: -.065em; }
.index-hero p { max-width: 43rem; margin: 1.8rem 0 0; color: #48443e; font-size: 1.08rem; }
.index-label { font: 600 .72rem/1 var(--sans); letter-spacing: .15em; text-transform: uppercase; color: var(--accent); margin-bottom: 1.5rem; }
.feed { padding: 0 0 8rem; }
.feed-article { padding: clamp(5.5rem, 10vw, 8.5rem) 0 clamp(6.5rem, 12vw, 10rem); border-bottom: 1px solid var(--rule-dark); }
.feed-article:last-child { border-bottom: 0; }
.feed-header { max-width: 58rem; margin-bottom: 3.4rem; }
.feed-header .kicker { margin-bottom: 1.2rem; }
.feed-title { max-width: 17ch; margin: 0; font: 700 clamp(2.55rem, 6vw, 4.2rem)/1.15 var(--serif); letter-spacing: -.055em; text-wrap: balance; }
.feed-title a { text-decoration: none; }
.feed-deck { max-width: 49rem; margin: 1.45rem 0 0; color: #3e3b36; font-size: 1.12rem; line-height: 1.78; }
.feed-meta { margin-top: 2rem; display: flex; flex-wrap: wrap; gap: .7rem 1.2rem; color: var(--muted); font: 500 .74rem/1.5 var(--sans); font-variant-numeric: tabular-nums; }
.feed-meta span + span::before { content: '·'; margin-right: 1.2rem; color: var(--faint); }
.feed-grid { display: grid; grid-template-columns: minmax(0, var(--measure)) minmax(180px, 1fr); gap: clamp(3rem, 8vw, 7.5rem); align-items: start; }
.feed-note { position: sticky; top: 2rem; color: var(--muted); font: .72rem/1.72 var(--sans); border-top: 1px solid var(--rule-dark); padding-top: .9rem; }
.feed-note .folio { display: block; margin-bottom: 1.1rem; color: var(--faint); font-size: 1.7rem; line-height: 1; font-variant-numeric: tabular-nums; }
.feed-permalink { margin-top: 4rem; padding-top: 1rem; border-top: 1px solid var(--rule); font: 600 .72rem/1.5 var(--sans); letter-spacing: .04em; text-transform: uppercase; }
.feed-permalink a { text-decoration: none; }

.style-guide { max-width: 54rem; padding: 5rem 0 8rem; }
.style-guide h1 { font-size: var(--step-4); line-height: 1.2; letter-spacing: -.045em; }
.swatch { display: inline-block; width: 1.2rem; height: 1.2rem; vertical-align: -.2rem; border: 1px solid var(--rule-dark); margin-right: .35rem; }
.type-sample-serif { font: 500 1.65rem/1.75 var(--serif); }
.type-sample-sans { font: 500 .92rem/1.7 var(--sans); }

.site-footer { border-top: 1px solid var(--rule-dark); padding: 2.2rem 0 3rem; color: var(--muted); font: .7rem/1.65 var(--sans); display: flex; justify-content: space-between; gap: 2rem; }
.site-footer a { text-decoration: none; }

@media (max-width: 820px) {
  body { font-size: 17px; line-height: 1.88; }
  .masthead { padding: 0 5vw; height: 58px; }
  .masthead .edition { display: none; }
  .page { width: min(90vw, 44rem); }
  .article-header { padding: 4.1rem 0 2.7rem; }
  h1.article-title { font-size: clamp(2.4rem, 11vw, 3.45rem); max-width: 15ch; }
  .deck { font-size: 1.02rem; }
  .article-grid { grid-template-columns: 1fr; gap: 0; padding-top: 3rem; }
  .margin-note { position: static; order: -1; margin-bottom: 2.7rem; padding: .9rem 0; display: grid; grid-template-columns: 4rem 1fr; gap: .9rem; }
  .margin-note .folio { margin: .1rem 0 0; }
  .pullquote { margin-left: 0; margin-right: 0; }
  .feed-grid { grid-template-columns: 1fr; gap: 0; }
  .feed-note { position: static; order: -1; margin-bottom: 2.5rem; display: grid; grid-template-columns: 4rem 1fr; gap: .9rem; }
  .feed-note .folio { margin: .1rem 0 0; }
  .feed-title { max-width: 15ch; }
  .index-hero h1 { max-width: 11ch; }
  .site-footer { display: block; }
  .site-footer > * + * { margin-top: .6rem; }
}

@media (max-width: 480px) {
  body { font-size: 16.5px; }
  .page { width: 88vw; }
  .article-body h2 { font-size: 1.65rem; margin-top: 3.15rem; }
  .table-wrap { width: 100vw; margin-left: calc((88vw - 100vw)/2); padding-left: 6vw; padding-right: 6vw; border-left: 0; border-right: 0; }
  table { min-width: 620px; }
  .article-meta span + span::before { display: none; }
  .article-meta { display: grid; gap: .35rem; }
}

@media print {
  @page { size: A4; margin: 18mm 18mm 20mm 18mm; }
  html, body { background: white; }
  body { font-size: 10.5pt; line-height: 1.75; }
  .masthead, .issue-nav, .site-footer, .margin-note, .feed-note { display: none !important; }
  .page { width: auto; max-width: none; margin: 0; }
  .article-header { padding: 0 0 12mm; }
  h1.article-title { font-size: 28pt; max-width: 15ch; }
  .article-grid, .feed-grid { display: block; padding: 12mm 0 0; }
  .feed-article { break-before: page; padding: 0; border: 0; }
  .feed-article:first-child { break-before: auto; }
  .article-body { max-width: none; }
  .article-body h2, .article-body h3 { break-after: avoid; }
  p, li, blockquote, figure, table { break-inside: avoid; }
  .figure img { max-height: 110mm; object-fit: contain; }
  a { text-decoration: none; }
  a[href^='http']::after { content: ' [' attr(href) ']'; font: 7pt/1.2 var(--sans); color: #666; word-break: break-all; }
}
'''


def inline(text: str) -> str:
    text = text.strip()
    # Render the small subset of LaTeX notation used by the magazine as readable Unicode
    # rather than exposing raw backslashes on the finished page.
    text = text.replace(r"\approx", "≈").replace(r"\theta", "θ")
    text = text.replace(r"\[", "").replace(r"\]", "").replace(r"\(", "").replace(r"\)", "").replace(r"\,", " ")
    text = html.escape(text)
    stash: list[str] = []
    def keep_code(m):
        stash.append(f"<code>{m.group(1)}</code>")
        return f"\x00{len(stash)-1}\x00"
    text = re.sub(r"`([^`]+)`", keep_code, text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r'<img src="\2" alt="\1">', text)
    def linkify(m):
        label, href = m.group(1), m.group(2)
        if href.startswith("../"):
            href = "https://github.com/kwj8677/gpt/blob/main/" + href[3:]
        return f'<a href="{href}">{label}</a>'
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", linkify, text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    for i, val in enumerate(stash):
        text = text.replace(f"\x00{i}\x00", val)
    return text


def md_to_html(md: str) -> tuple[str, str, str]:
    lines = md.replace("\r\n", "\n").split("\n")
    title = ""
    evidence = ""
    out: list[str] = []
    i = 0
    first_quote = True
    while i < len(lines):
        raw = lines[i]
        s = raw.strip()
        if not s:
            i += 1
            continue
        if s.startswith("# ") and not title:
            title = s[2:].strip()
            i += 1
            continue
        if s.startswith("```"):
            lang = s[3:].strip()
            buf = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            out.append(f'<pre data-lang="{html.escape(lang)}"><code>{html.escape(chr(10).join(buf))}</code></pre>')
            continue
        if s.startswith("| ") or (s.startswith("|") and s.endswith("|")):
            rows = []
            while i < len(lines):
                t = lines[i].strip()
                if not (t.startswith("|") and t.endswith("|")):
                    break
                cells = [c.strip() for c in t.strip("|").split("|")]
                rows.append(cells)
                i += 1
            if rows:
                header = rows[0]
                body = [r for r in rows[1:] if not all(re.fullmatch(r":?-{2,}:?", c.replace(" ", "")) for c in r)]
                tparts = ['<div class="table-wrap"><table><thead><tr>']
                tparts.extend(f'<th>{inline(c)}</th>' for c in header)
                tparts.append('</tr></thead><tbody>')
                for row in body:
                    tparts.append('<tr>')
                    tparts.extend(f'<td>{inline(c)}</td>' for c in row)
                    tparts.append('</tr>')
                tparts.append('</tbody></table></div>')
                out.append(''.join(tparts))
            continue
        if s.startswith("!["):
            m = re.match(r"!\[([^\]]*)\]\(([^)]+)\)", s)
            if m:
                alt, src = m.groups()
                out.append(f'<figure class="figure"><img src="{html.escape(src)}" alt="{html.escape(alt)}"><figcaption>{html.escape(alt)}</figcaption></figure>')
                i += 1
                continue
        if s.startswith(">"):
            buf = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                buf.append(lines[i].strip()[1:].strip())
                i += 1
            text = " ".join(buf)
            if first_quote:
                evidence = re.sub(r"\*\*", "", text)
                out.append(f'<aside class="evidence-note">{inline(text)}</aside>')
                first_quote = False
            else:
                out.append(f'<blockquote class="pullquote"><p>{inline(text)}</p></blockquote>')
            continue
        if s.startswith("## "):
            out.append(f'<h2>{inline(s[3:])}</h2>')
            i += 1
            continue
        if s.startswith("### "):
            out.append(f'<h3>{inline(s[4:])}</h3>')
            i += 1
            continue
        if s in ("---", "***"):
            out.append('<hr>')
            i += 1
            continue
        if re.match(r"^[-*] ", s):
            items = []
            while i < len(lines) and re.match(r"^[-*] ", lines[i].strip()):
                items.append(re.sub(r"^[-*] ", "", lines[i].strip()))
                i += 1
            out.append('<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + '</ul>')
            continue
        if re.match(r"^\d+[.)] ", s):
            items = []
            while i < len(lines) and re.match(r"^\d+[.)] ", lines[i].strip()):
                items.append(re.sub(r"^\d+[.)] ", "", lines[i].strip()))
                i += 1
            out.append('<ol>' + ''.join(f'<li>{inline(x)}</li>' for x in items) + '</ol>')
            continue
        # paragraph: join consecutive ordinary lines
        buf = [s]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt or nxt.startswith(("#", ">", "```", "|", "![", "---")) or re.match(r"^[-*] ", nxt) or re.match(r"^\d+[.)] ", nxt):
                break
            buf.append(nxt)
            i += 1
        out.append(f'<p>{inline(" ".join(buf))}</p>')
    # use first substantial paragraph after evidence as deck
    deck = ""
    for fragment in out:
        if fragment.startswith("<p>"):
            deck = re.sub(r"<[^>]+>", "", fragment)
            if len(deck) > 30:
                break
    return title, evidence, "\n".join(out)


def shell(title: str, issue: str, category: str, evidence_type: str, body: str, deck: str, prev_link: str | None, next_link: str | None) -> str:
    nav = ['<nav class="issue-nav">']
    nav.append(f'<a href="{prev_link}">← 이전 호</a>' if prev_link else '<span></span>')
    nav.append(f'<a href="{next_link}">다음 호 →</a>' if next_link else '<span></span>')
    nav.append('</nav>')
    return f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} — Magazine Editions</title><meta name="description" content="{html.escape(deck[:155])}">
<link rel="stylesheet" href="style.css"></head><body>
<header class="masthead"><a href="index.html">MAGAZINE COLUMN</a><span class="edition">Ongoing publication · 2026</span><a href="style-guide.html">TYPE / STYLE</a></header>
<main class="page">
<header class="article-header"><div class="kicker">COLUMN {issue}</div><h1 class="article-title">{html.escape(title)}</h1><p class="deck">{html.escape(deck)}</p><div class="article-meta"><span>{html.escape(evidence_type)}</span><span>2026.08.31</span><span>Facts · inference · hypothesis separated</span></div></header>
<div class="article-grid"><article class="article-body">{body}{''.join(nav)}</article>
<aside class="margin-note"><span class="folio">{issue}</span><div><strong>읽는 법</strong>이 판본은 원 연구를 덮어쓰지 않는다. 사실, 해석, 실무 가설의 강도를 구분하고 반대가설과 반증 조건을 함께 둔다.</div></aside></div>
</main><footer class="page site-footer"><span>Magazine Editions · Source-preserving editorial series</span><span><a href="https://github.com/kwj8677/gpt/tree/main/magazine">Source & notes ↗</a></span></footer></body></html>'''


def build_index(parsed: list[tuple]) -> str:
    articles = []
    for no, fn, title, category, typ, body, deck in reversed(parsed):
        page = fn.replace('.ko.md', '.html')
        # The deck already repeats the first normal paragraph; remove that paragraph
        # from the continuous feed so the opening is not duplicated.
        feed_body = re.sub(r"<p>.*?</p>", "", body, count=1, flags=re.S)
        articles.append(f'''<section class="feed-article" id="column-{no}">
<header class="feed-header"><div class="kicker">COLUMN {no} · 2026.08.31</div><h2 class="feed-title">{html.escape(title)}</h2><p class="feed-deck">{html.escape(deck)}</p><div class="feed-meta"><span>{html.escape(typ)}</span><span>Facts · inference · hypothesis separated</span></div></header>
<div class="feed-grid"><article class="article-body">{feed_body}<div class="feed-permalink"><a href="{page}">Permalink · 이 글만 보기 ↗</a></div></article><aside class="feed-note"><span class="folio">{no}</span><div>원 연구와 메모는 별도 보존한다. 이 지면에서는 근거의 강도, 반대가설, 반증 조건을 함께 편집한다.</div></aside></div>
</section>''')
    return f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Magazine Column</title><meta name="description" content="정기적으로 이어지는 한국어 독립 매거진 칼럼."><link rel="stylesheet" href="style.css"></head><body>
<header class="masthead"><a href="index.html">MAGAZINE COLUMN</a><span class="edition">Ongoing publication · newest first</span><a href="style-guide.html">TYPE / STYLE</a></header>
<main class="page"><section class="index-hero"><div class="index-label">Ongoing column</div><h1>칼럼은<br>아래로 쌓인다.</h1><p>새 글이 가장 위에 놓이고, 이전 글은 그 아래로 이어진다. 지금은 주제를 억지로 분류하지 않는다. 수치가 있는 주장은 표와 그래프로, 판단은 반대가설과 함께 기록한다.</p></section><div class="feed">{''.join(articles)}</div></main>
<footer class="page site-footer"><span>새 글은 위에 추가되고, 분류는 충분히 쌓인 뒤 실제 패턴을 보고 만든다.</span><span><a href="https://github.com/kwj8677/gpt/tree/main/magazine">Source & notes ↗</a></span></footer></body></html>'''

STYLE_GUIDE = '''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Typography & Editorial Style — Magazine Editions</title><link rel="stylesheet" href="style.css"></head><body>
<header class="masthead"><a href="index.html">MAGAZINE EDITIONS</a><span class="edition">Editorial system</span><a href="style-guide.html">TYPE / STYLE</a></header><main class="page style-guide">
<div class="index-label">Typography / Editorial system</div><h1>읽기 위해 만든 지면</h1><p class="type-sample-serif">장식보다 리듬. 제목의 크기보다 본문의 폭. 숫자를 강조하기보다 단위를 명확히. 이 지면의 목표는 ‘고급스러워 보이기’가 아니라 긴 한국어 문장을 오래 읽어도 눈의 피로와 정보의 위계를 동시에 잃지 않는 것이다.</p>
<h2>활자</h2><p><strong>본문</strong> — Noto Serif KR → Nanum Myeongjo → AppleMyungjo/Batang. 18px, 약 1.92 행간. 데스크톱 본문 폭은 약 42rem으로 제한해 대략 34–42자의 한국어 읽기 폭을 목표로 한다.</p><p class="type-sample-sans"><strong>정보층</strong> — Noto Sans KR → Pretendard → 시스템 고딕. 캡션·근거 상태·표·출처·폴리오에는 고딕을 써 본문과 기능을 분리한다. 숫자는 tabular numerals를 사용한다.</p>
<h2>위계</h2><p>H1은 2.65–3.65rem의 제한된 스케일, H2는 본문 리듬을 끊는 얇은 룰과 함께 사용한다. 한국어 제목에는 과도한 영문식 자간 벌림 대신 약한 음수 자간과 균형 줄바꿈을 쓴다. 본문은 <code>word-break: keep-all</code>과 palt/kern을 적용한다.</p>
<h2>표와 그래프</h2><p>표는 카드가 아니라 편집표다. 상단 2px 룰, 얇은 행 구분선, 명시적 단위, tabular numerals를 사용한다. 그래프는 측정값 또는 명시된 산식만 그린다. 추정값을 그려야 할 경우 ‘추정’임을 축·캡션에 표시하고, 단지 시각적으로 풍부해 보이기 위해 그래프를 만들지 않는다.</p>
<h2>색과 종이</h2><p><span class="swatch" style="background:#f4f1e8"></span>Paper #F4F1E8 &nbsp; <span class="swatch" style="background:#1a1916"></span>Ink #1A1916 &nbsp; <span class="swatch" style="background:#304e5c"></span>Accent #304E5C. 인쇄물의 미색 종이와 먹색 대비를 참고하되 장식적 그라디언트나 유리 효과는 쓰지 않는다.</p>
<h2>편집 원칙</h2><ol><li>원 연구를 보존하고 매거진 판은 별도 파일로 둔다.</li><li>사실과 추론의 문장 강도를 다르게 쓴다.</li><li>저자 정의 용어는 표준 학술용어처럼 포장하지 않는다.</li><li>가장 강한 반대가설과 ‘무엇이 결론을 바꿀지’를 싣는다.</li><li>국가·브랜드·개인의 취향을 메커니즘의 증거로 사용하지 않는다.</li></ol><h2>발행 구조</h2><p>메인은 최신 칼럼부터 본문 전체가 연속으로 이어지는 단일 지면이다. 개별 HTML은 공유·인용용 permalink로만 유지한다. 카테고리는 미리 정하지 않고 글이 충분히 쌓인 뒤 실제 주제 패턴을 관찰해 만든다.</p>
<h2>모바일과 인쇄</h2><p>820px 이하에서는 사이드노트를 본문 위로 이동하고, 480px 이하 표는 가로 스크롤을 허용한다. A4 인쇄 CSS에서는 내비게이션을 제거하고 heading·figure의 페이지 분리를 억제한다. 웹 폰트가 실패해도 한국어 시스템 명조/고딕으로 위계가 유지된다.</p>
</main><footer class="page site-footer"><span>Magazine Editions · typography guide</span><span><a href="index.html">← Index</a></span></footer></body></html>'''


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    ASSETS.mkdir(parents=True, exist_ok=True)
    (ROOT / "docs" / ".nojekyll").write_text("", encoding="utf-8")
    (OUT / "style.css").write_text(CSS, encoding="utf-8")
    if (SRC / "assets").exists():
        for p in (SRC / "assets").iterdir():
            if p.is_file():
                shutil.copy2(p, ASSETS / p.name)
    parsed = []
    for no, fn, fallback_title, category, typ in ISSUES:
        md_path = SRC / fn
        if not md_path.exists():
            raise FileNotFoundError(md_path)
        md = md_path.read_text(encoding="utf-8")
        title, evidence, body = md_to_html(md)
        title = title or fallback_title
        # derive a readable deck from first normal paragraph
        m = re.search(r"<p>(.*?)</p>", body, re.S)
        deck = re.sub(r"<[^>]+>", "", m.group(1)) if m else evidence
        parsed.append((no, fn, title, category, typ, body, html.unescape(deck)))
    for idx, item in enumerate(parsed):
        no, fn, title, category, typ, body, deck = item
        prev_link = parsed[idx-1][1].replace('.ko.md', '.html') if idx > 0 else None
        next_link = parsed[idx+1][1].replace('.ko.md', '.html') if idx + 1 < len(parsed) else None
        out_name = fn.replace('.ko.md', '.html')
        (OUT / out_name).write_text(shell(title, no, category, typ, body, deck, prev_link, next_link), encoding="utf-8")
    (OUT / "index.html").write_text(build_index(parsed), encoding="utf-8")
    (OUT / "style-guide.html").write_text(STYLE_GUIDE, encoding="utf-8")
    root_index = ROOT / "docs" / "index.html"
    root_index.write_text('''<!doctype html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="0; url=magazine/"><title>Magazine Editions</title></head><body><p><a href="magazine/">Magazine Editions</a></p></body></html>''', encoding="utf-8")
    print(f"built {len(parsed)} issues in {OUT}")

if __name__ == "__main__":
    main()
