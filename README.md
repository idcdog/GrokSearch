![这是图片](./images/title.png)
<div align="center">

[English](./docs/README_EN.md) | 简体中文

**Grok Search 是一个直接调用 Grok/OpenAI 兼容 API 的轻量级搜索客户端（不依赖 MCP）**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

</div>

---

## 概述

Grok Search 提供一个简单的 CLI 与 Python API，用于向 OpenAI 兼容的 Grok 接口发起搜索/抓取请求。它不依赖 MCP，适合直接集成到脚本、服务或 Codex/Claude 的自定义 Skill 流程中。

## 功能特性

- ✅ OpenAI 兼容接口，环境变量配置
- ✅ 实时网络搜索 + 网页内容抓取
- ✅ 支持指定搜索平台（Twitter、Reddit、GitHub 等）
- ✅ 配置测试（连接测试 + API Key 脱敏）
- ✅ 动态模型切换（支持切换不同 Grok 模型并持久化保存）
- ✅ 自动时间注入（搜索时自动获取本地时间，确保时间相关查询的准确性）

## 安装

推荐使用 `uvx` 直接运行（无需安装）：

```bash
uvx --from git+https://github.com/GuDaStudio/GrokSearch grok-search --help
```

或安装到本地环境：

```bash
pip install git+https://github.com/GuDaStudio/GrokSearch
```

## 配置

优先使用环境变量（优先级高于配置文件）：

```bash
export GROK_API_URL="https://your-api-endpoint.com/v1"
export GROK_API_KEY="your-api-key-here"
```

可选：在配置文件中设置 API 与默认模型（`~/.config/grok-search/config.json`）：

```json
{
  "api_url": "https://your-api-endpoint.com/v1",
  "api_key": "your-api-key-here",
  "model": "grok-4-fast"
}
```

## 使用方式（CLI）

### 搜索

```bash
grok-search search "最近的 Claude Code 更新" --platform "GitHub" --min-results 3 --max-results 8
```

### 抓取网页内容

```bash
grok-search fetch "https://example.com/article"
```

### 查看配置并测试连接

```bash
grok-search config
```

## 使用方式（Python）

```python
import asyncio
from grok_search import search, fetch, get_config_info

async def main():
    results = await search("最近的 Claude Code 更新", platform="GitHub")
    print(results)

    content = await fetch("https://example.com/article")
    print(content)

    config = await get_config_info()
    print(config)

asyncio.run(main())
```

## 常见问题

- **默认模型是什么？**
  默认模型为 `grok-4-fast`，可通过配置文件覆盖。

- **配置文件在哪里？**
  `~/.config/grok-search/config.json`。

---

如需作为 Codex/Claude 的 Skill 使用，只需在 Skill 中调用 CLI 或 Python API 即可。
