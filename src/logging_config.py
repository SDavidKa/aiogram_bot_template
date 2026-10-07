import logging
import sys
import structlog

from src.config import LOG_LEVEL, LOG_FORMAT


def configure_logging():
    """
    Настройка стандартного логирования так,
    чтобы structlog и все сторонние библиотеки писали через единый формат.
    """
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, LOG_LEVEL, logging.INFO),
    )

    # Общие процессоры
    shared_processors = [
        structlog.stdlib.add_log_level,
        structlog.stdlib.add_logger_name,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.dict_tracebacks,
    ]

    if LOG_FORMAT == "json":
        renderer = structlog.processors.JSONRenderer(
            sort_keys=True,
            ensure_ascii=False,
            default=str,
        )
    else:
        renderer = structlog.dev.ConsoleRenderer(colors=True)

    structlog.configure(
        processors=shared_processors + [renderer],
        wrapper_class=structlog.stdlib.BoundLogger,
        logger_factory=structlog.stdlib.LoggerFactory(),
        cache_logger_on_first_use=True,
    )


configure_logging()
logger = structlog.get_logger()
