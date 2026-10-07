import httpx

from src.logging_config import logger


async def safe_api_call(coro):
    """
    Универсальная обёртка для безопасных API вызовов
    coro — это корутина (await client.get(...))
    """
    try:
        response: httpx.Response = await coro
        return response
    except (httpx.ConnectError, httpx.ReadTimeout, httpx.RemoteProtocolError) as e:
        logger.error(f"API network error: {e}")
        return None
    except Exception as e:
        logger.exception(f"Unexpected API error: {e}")
        return None
