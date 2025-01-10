import asyncio

from aiogram import Dispatcher, Bot
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from services.PostgresStorage import PostgresStorage
from services.logging_config import logger
from config import PostgresConfig, BotConfig
from routers import router as main_router

storage = PostgresStorage(dsn=PostgresConfig.URL)


async def on_startup() -> None:
    await storage.connect()


async def main() -> None:
    bot = Bot(token=BotConfig.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=storage)
    dp.startup.register(on_startup)
    dp.include_router(router=main_router)

    try:
        await dp.start_polling(bot)
        logger.info('Bot starting')
    finally:
        await dp.storage.close()


if __name__ == '__main__':
    asyncio.run(main())
