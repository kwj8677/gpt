from __future__ import annotations

import argparse
import json
from pathlib import Path

from .core import RankResult, SearchRankingTracker, load_config, write_csv


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Track keyword search rankings for configured target sites.")
    parser.add_argument("--config", default="rank-tracker.json", help="JSON config path")
    parser.add_argument("--output", default="data/rank-history.csv", help="CSV history output path")
    parser.add_argument("--limit", type=int, default=30, help="Maximum organic results to inspect per keyword")
    parser.add_argument("--engine-url", default="https://duckduckgo.com/html/?q={query}", help="Search URL template with {query}")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON summary")
    return parser


def serialize_result(result: RankResult) -> dict[str, object]:
    return {
        "checked_at": result.checked_at,
        "keyword": result.keyword,
        "target": result.target,
        "status": result.status,
        "best_rank": result.best_rank,
        "matches": [match.__dict__ for match in result.matches],
        "total_results_checked": result.total_results_checked,
    }


def main() -> int:
    args = build_parser().parse_args()
    keywords, targets = load_config(args.config)
    tracker = SearchRankingTracker(targets, engine_url=args.engine_url)
    results = tracker.track(keywords, limit=args.limit)
    write_csv(args.output, results)

    if args.json:
        print(json.dumps([serialize_result(result) for result in results], ensure_ascii=False, indent=2))
    else:
        for result in results:
            rank = result.best_rank if result.best_rank is not None else "미노출"
            print(f"{result.keyword} | {result.target} | {rank} | 확인 결과 {result.total_results_checked}개")
        print(f"Saved history: {Path(args.output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
