from aiogram import Router

from .post_kb_callback_handlers import router as post_kb_callback_router

router = Router(name=__name__)

router.include_routers(
    post_kb_callback_router,
)