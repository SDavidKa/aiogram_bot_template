import logging
import structlog
import sys
import json
from logging.handlers import RotatingFileHandler
from src.config import LOG_LEVEL


# Кастомный JSON-рендерер с поддержкой UTF-8
class UTF8JSONRenderer(structlog.processors.JSONRenderer):
    def __call__(self, logger, name, event_dict):
        return json.dumps(event_dict, ensure_ascii=False)


# Настройка стандартного логирования
def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, LOG_LEVEL, "INFO"))

    log_format = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    file_handler = RotatingFileHandler(
        "bot.log", maxBytes=5_000_000, backupCount=5, encoding="utf-8"
    )
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)


# Настройка structlog
def configure_structlog():
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.stdlib.add_log_level,
            structlog.stdlib.add_logger_name,
            UTF8JSONRenderer(),
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )


# Инициализация логирования
configure_logging()
configure_structlog()

logger = structlog.get_logger()
