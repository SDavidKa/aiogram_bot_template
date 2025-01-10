from aiogram import Router

from .admin_commands_hanlers import router as admin_commands_router

router = Router(name=__name__)

router.include_routers(
    admin_commands_router,
)