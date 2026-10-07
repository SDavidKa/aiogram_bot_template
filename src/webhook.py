import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web
from aiogram import Bot

from src.config import WEBAPP_HOST, WEBAPP_PORT, BASE_WEBHOOK_PATH, BASE_WEBHOOK_URL, WEBHOOK_SECRET_TOKEN
from src.api.client import client
from src.app import create_dispatcher, create_bot
from src.logging_config import logger


async def on_startup(bot: Bot) -> None:
    me = await bot.get_me()
    logger.warning(f"Started bot: {me.username}")
    url = f"{BASE_WEBHOOK_URL}{BASE_WEBHOOK_PATH}/webhook"

    webhook_info = await bot.get_webhook_info()
    logger.debug(f"webhook info: {webhook_info}")
    logger.debug(f"current url: {url}, webhook info url: {webhook_info.url}")
    if webhook_info.url != url:
        await bot.delete_webhook(drop_pending_updates=False)

        await bot.set_webhook(
            url=url,
            secret_token=WEBHOOK_SECRET_TOKEN,
        )
        logger.info("Successfully setup webhook")


async def on_shutdown(bot: Bot) -> None:
    await client.aclose()
    logger.info("httpx клиент закрыт")


def create_prepared_web_app() -> web.Application:
    bot = create_bot()
    dp = create_dispatcher()
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    app = web.Application()

    webhook_request_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
        secret_token=WEBHOOK_SECRET_TOKEN,
        handle_in_background=False,
    )
    webhook_request_handler.register(app, path=f"{BASE_WEBHOOK_PATH}/webhook")
    setup_application(app, dp, bot=bot)

    return app


def main():
    try:
        app = create_prepared_web_app()

        web.run_app(
            app,
            host=WEBAPP_HOST,
            port=int(WEBAPP_PORT),
        )
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()
