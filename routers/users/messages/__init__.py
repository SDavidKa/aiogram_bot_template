from aiogram import Router

from .echo import router as echo_router

router = Router(name=__name__)

# Оставить в конце, чтобы этот роутер вызывался последним
router.include_router(
    echo_router
)
