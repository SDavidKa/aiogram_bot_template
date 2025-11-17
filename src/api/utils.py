import httpx

from src.logging_config import logger


async def safe_api_call(coro):
    """
    Универсальная обёртка для безопасных API вызовов
    coro — это корутина (await client.get(...))
    """
    try:
        response = await coro
        response.raise_for_status()
        return response
    except httpx.HTTPStatusError as e:
        logger.error(
            f"API request failed: {e}",
            status_code=e.response.status_code,
            error=str(e)
        )
        raise
    except Exception as e:
        logger.exception(f"ANOTHER API request failed: {e}")
        raise
