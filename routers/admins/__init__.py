from aiogram import Router

from .commands import router as admin_commands_router
from .callback import router as admin_callback_router

router = Router(name=__name__)

router.include_routers(
    admin_commands_router,
    admin_callback_router,
)