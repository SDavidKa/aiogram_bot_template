import os


class BotConfig:
    TOKEN = os.getenv("BOT_TOKEN")
    WEBHOOK_URL = os.getenv("WEBHOOK_URL")
    WEBHOOK_PATH = f"/webhook/{TOKEN}"
    WEBAPP_HOST = os.getenv("WEBAPP_HOST")
    WEBAPP_PORT = os.getenv("WEBAPP_PORT")


class PostgresConfig:
    USER = os.getenv("DB_USER")
    PASS = os.getenv("DB_PASS")
    HOST = os.getenv("DB_HOST")
    PORT = os.getenv("DB_PORT")
    NAME = os.getenv("DB_NAME")
    SCHEMA = os.getenv("DB_SCHEMA")

    URL = f"postgresql+asyncpg://{USER}:{PASS}@{HOST}:{PORT}/{NAME}"
