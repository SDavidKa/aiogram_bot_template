import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from src.logging_config import logger
from src.api.client import client
from src.app import create_dispatcher, create_bot


async def main() -> None:
    dp = create_dispatcher()
    bot = create_bot()
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception("Ошибка в работе бота", exception=e)
    finally:
        await client.aclose()
        logger.info("httpx клиент закрыт")


if __name__ == "__main__":
    asyncio.run(main())
