from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from src.config import TELEGRAM_TOKEN
from src.routers import router as main_router


def create_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(main_router)

    return dp


def create_bot() -> Bot:
    bot = Bot(
        token=TELEGRAM_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    return bot
