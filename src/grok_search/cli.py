import argparse
import asyncio
import sys

from .app import fetch, get_config_info, search


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="grok-search",
        description="Direct Grok Search client (no MCP required).",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    search_parser = subparsers.add_parser("search", help="Run web search.")
    search_parser.add_argument("query", help="Search query text.")
    search_parser.add_argument("--platform", default="", help="Platform hints, e.g. GitHub, Reddit.")
    search_parser.add_argument("--min-results", type=int, default=3, dest="min_results")
    search_parser.add_argument("--max-results", type=int, default=10, dest="max_results")
    search_parser.add_argument("--model", default=None, help="Override model ID.")

    fetch_parser = subparsers.add_parser("fetch", help="Fetch a URL as structured Markdown.")
    fetch_parser.add_argument("url", help="Target URL.")
    fetch_parser.add_argument("--model", default=None, help="Override model ID.")

    config_parser = subparsers.add_parser("config", help="Show configuration and test connection.")
    config_parser.add_argument("--json", action="store_true", help="Output JSON only.")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        if args.command == "search":
            result = asyncio.run(
                search(
                    args.query,
                    platform=args.platform,
                    min_results=args.min_results,
                    max_results=args.max_results,
                    model=args.model,
                )
            )
        elif args.command == "fetch":
            result = asyncio.run(fetch(args.url, model=args.model))
        elif args.command == "config":
            result = asyncio.run(get_config_info())
        else:
            parser.error("Unknown command")
            return 2
    except KeyboardInterrupt:
        return 130
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
