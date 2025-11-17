import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import asyncio

from aiogram import Dispatcher, Bot

from config import bot
from routers import router as main_router
from src.logging_config import logger
from src.api.client import client


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(main_router)

    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.exception("Ошибка в работе бота", exception=e)
    finally:
        await client.aclose()
        logger.info("httpx клиент закрыт")


if __name__ == "__main__":
    asyncio.run(main())
