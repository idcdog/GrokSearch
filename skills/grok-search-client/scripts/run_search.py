import argparse
import asyncio
import sys
from pathlib import Path

def find_project_root(start: Path) -> Path | None:
    for candidate in [start, *start.parents]:
        if (candidate / "pyproject.toml").is_file():
            return candidate
    return None


PROJECT_ROOT = find_project_root(Path(__file__).resolve())
if PROJECT_ROOT:
    SRC_PATH = PROJECT_ROOT / "src"
    if SRC_PATH.is_dir() and str(SRC_PATH) not in sys.path:
        sys.path.insert(0, str(SRC_PATH))

from grok_search import search


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run Grok Search via Python API.")
    parser.add_argument("query", help="Search query text")
    parser.add_argument("--platform", default="", help="Platform hints (e.g. GitHub)")
    parser.add_argument("--min-results", type=int, default=3, dest="min_results")
    parser.add_argument("--max-results", type=int, default=10, dest="max_results")
    parser.add_argument("--model", default=None, help="Override model ID")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    result = asyncio.run(
        search(
            args.query,
            platform=args.platform,
            min_results=args.min_results,
            max_results=args.max_results,
            model=args.model,
        )
    )
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
