__all__ = ("router")

from aiogram import Router

from routers.users.commands import router as commands_router
from routers.users.messages import router as messages_router
from .admins import router as admins_router

router = Router(name=__name__)

router.include_routers(
    commands_router,
    admins_router,
    messages_router,
)
