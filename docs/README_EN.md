![Image](../images/title.png)
<div align="center">

English | [简体中文](../README.md)

**Grok Search is a lightweight CLI/Python client for Grok/OpenAI-compatible APIs (no MCP required).**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

</div>

---

## Overview

Grok Search provides a simple CLI and Python API to send search/fetch requests to an OpenAI-compatible Grok endpoint. It does not depend on MCP, making it easy to embed in scripts, services, or Codex/Claude skills.

## Features

- ✅ OpenAI-compatible API with env-based configuration
- ✅ Real-time web search and page fetch
- ✅ Platform hints (Twitter, Reddit, GitHub, etc.)
- ✅ Config diagnostics (connection test + masked API key)
- ✅ Model switching (persisted to a local config file)
- ✅ Automatic time context injection for time-sensitive queries

## Install

Run with `uvx` (no install required):

```bash
uvx --from git+https://github.com/GuDaStudio/GrokSearch grok-search --help
```

Or install locally:

```bash
pip install git+https://github.com/GuDaStudio/GrokSearch
```

## Configuration

Set required environment variables:

```bash
export GROK_API_URL="https://your-api-endpoint.com/v1"
export GROK_API_KEY="your-api-key-here"
```

Optional default model (persisted to `~/.config/grok-search/config.json`):

```json
{
  "model": "grok-2-latest"
}
```

## CLI Usage

### Search

```bash
grok-search search "latest Claude Code updates" --platform "GitHub" --min-results 3 --max-results 8
```

### Fetch page content

```bash
grok-search fetch "https://example.com/article"
```

### Show config and test connection

```bash
grok-search config
```

## Python Usage

```python
import asyncio
from grok_search import search, fetch, get_config_info

async def main():
    results = await search("latest Claude Code updates", platform="GitHub")
    print(results)

    content = await fetch("https://example.com/article")
    print(content)

    config = await get_config_info()
    print(config)

asyncio.run(main())
```

## FAQ

- **Default model?**
  The default model is `grok-4-fast`, unless overridden in config.

- **Where is the config file?**
  `~/.config/grok-search/config.json`.

---

To use this as a Codex/Claude skill, invoke the CLI or Python API from your skill workflow.
