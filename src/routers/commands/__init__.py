from aiogram import Router

from .base import router as base_commands_router

router = Router(name=__name__)

router.include_routers(
    base_commands_router,
)