---
name: grok-search-client
description: Use when you need to run Grok/OpenAI-compatible web search or fetch via the grok-search CLI or Python API, especially inside Claude/Codex skills that should call a local script and return structured JSON/Markdown results.
---

# Grok Search Client

## Overview

Use this skill to invoke the grok-search CLI or Python API directly (no MCP). It is ideal for Claude/Codex skills that need deterministic commands for web search or page fetch.

## Quick Start

1. Export required environment variables.
2. Run the CLI or the sample script.
3. Return the JSON/Markdown output to the user.

```bash
export GROK_API_URL="https://your-api-endpoint.com/v1"
export GROK_API_KEY="your-api-key-here"
```

## Tasks

### 1) Web search (JSON)

Prefer the CLI for simple calls:

```bash
grok-search search "Your query" --platform "GitHub" --min-results 3 --max-results 8
```

Or use the bundled script:

```bash
python skills/grok-search-client/scripts/run_search.py "Your query" --platform "GitHub"
```

### 2) Web fetch (Markdown)

```bash
grok-search fetch "https://example.com/article"
```

### 3) Config diagnosis

```bash
grok-search config
```

## Output handling

- `search` returns a JSON array of `{title, url, description}` objects.
- `fetch` returns structured Markdown with metadata and content sections.
- Always pass raw output back to the user without adding extra wrapping text.

## Resources

### scripts/
- `run_search.py`: Example script that calls the Python API for search.

### references/
Empty by default. Add local guidance or API notes here if needed.
