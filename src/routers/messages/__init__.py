from aiogram import Router

from .base import router as base_message_router

from .echo import router as echo_message_router

router = Router(name=__name__)

router.include_routers(
    base_message_router,
)

# НЕ добавлять сюда другие роутеры, echo должен быть в самом конце, чтобы не сломать
router.include_router(echo_message_router)
