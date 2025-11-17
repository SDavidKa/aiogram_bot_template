import os
from aiogram.enums import ParseMode
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
DJANGO_API_URL = os.getenv("DJANGO_API_URL")
DJANGO_API_TOKEN = os.getenv("DJANGO_API_TOKEN")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

bot = Bot(token=TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
