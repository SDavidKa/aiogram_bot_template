from aiogram.filters import Filter
from aiogram.types import Message

from src.config import ADMIN_TG_ID


class IsAdmin(Filter):
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == ADMIN_TG_ID
