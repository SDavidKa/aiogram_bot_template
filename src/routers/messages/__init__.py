from aiogram import Router

from .echo import router as echo_router

router = Router(name=__name__)

# НЕ добавлять сюда другие роутеры, echo должен быть в самом конце, чтобы не сломать
router.include_router(echo_router)
