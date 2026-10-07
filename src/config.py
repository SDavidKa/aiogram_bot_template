import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_WEBHOOK_PATH = os.getenv("BASE_WEBHOOK_PATH")
BASE_URL = os.getenv("BASE_URL")
BASE_WEBHOOK_URL = os.getenv("BASE_WEBHOOK_URL")
WEBHOOK_SECRET_TOKEN = os.getenv("WEBHOOK_SECRET_TOKEN")
WEBAPP_HOST = os.getenv("WEBAPP_HOST")
WEBAPP_PORT = os.getenv("WEBAPP_PORT")
DJANGO_API_URL = os.getenv("DJANGO_API_URL")
DJANGO_API_TOKEN = os.getenv("DJANGO_API_TOKEN")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
LOG_FORMAT = os.getenv("LOG_FORMAT", "pretty").lower()
ADMIN_TG_ID = int(os.getenv("ADMIN_TG_ID")) if os.getenv("ADMIN_TG_ID") else None