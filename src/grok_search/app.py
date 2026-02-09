import json
from typing import Optional

import httpx

from .config import config
from .providers.grok import GrokSearchProvider


async def search(
    query: str,
    platform: str = "",
    min_results: int = 3,
    max_results: int = 10,
    model: Optional[str] = None,
) -> str:
    api_url = config.grok_api_url
    api_key = config.grok_api_key
    selected_model = model or config.grok_model
    provider = GrokSearchProvider(api_url, api_key, selected_model)
    return await provider.search(query, platform, min_results, max_results)


async def fetch(url: str, model: Optional[str] = None) -> str:
    api_url = config.grok_api_url
    api_key = config.grok_api_key
    selected_model = model or config.grok_model
    provider = GrokSearchProvider(api_url, api_key, selected_model)
    return await provider.fetch(url)


async def get_config_info() -> str:
    config_info = config.get_config_info()
    test_result = {
        "status": "未测试",
        "message": "",
        "response_time_ms": 0,
    }

    try:
        api_url = config.grok_api_url
        api_key = config.grok_api_key
        models_url = f"{api_url.rstrip('/')}/models"

        import time

        start_time = time.time()
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(
                models_url,
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json",
                },
            )

        response_time = (time.time() - start_time) * 1000
        test_result["response_time_ms"] = round(response_time, 2)

        if response.status_code == 200:
            test_result["status"] = "✅ 连接成功"
            test_result["message"] = f"成功获取模型列表 (HTTP {response.status_code})"
            try:
                models_data = response.json()
                if "data" in models_data and isinstance(models_data["data"], list):
                    model_count = len(models_data["data"])
                    test_result["message"] += f"，共 {model_count} 个模型"
                    model_names = []
                    for model in models_data["data"]:
                        if isinstance(model, dict) and "id" in model:
                            model_names.append(model["id"])
                    if model_names:
                        test_result["available_models"] = model_names
            except json.JSONDecodeError:
                pass
        else:
            test_result["status"] = "⚠️ 连接异常"
            test_result["message"] = f"HTTP {response.status_code}: {response.text[:100]}"
    except httpx.TimeoutException:
        test_result["status"] = "❌ 连接超时"
        test_result["message"] = "请求超时（10秒），请检查网络连接或 API URL"
    except httpx.RequestError as exc:
        test_result["status"] = "❌ 连接失败"
        test_result["message"] = f"网络错误: {str(exc)}"
    except ValueError as exc:
        test_result["status"] = "❌ 配置错误"
        test_result["message"] = str(exc)
    except Exception as exc:
        test_result["status"] = "❌ 测试失败"
        test_result["message"] = f"未知错误: {str(exc)}"

    config_info["connection_test"] = test_result
    return json.dumps(config_info, ensure_ascii=False, indent=2)
