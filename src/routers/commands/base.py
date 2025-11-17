from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown
from aiogram.types import ReplyKeyboardRemove, Message

from src.logging_config import logger
from src.states.filtration import Filtration
from src.states.contact import ContactInfo
from src.keyboards.inlines.common import get_filter_type_markup
from src.keyboards.replies.common import get_request_contact_markup
from src.api.endpoints.users import get_user_info_by_id
from src.utils.methods import send_group_info
from src.config import bot

router = Router(name=__name__)


@router.message(CommandStart())
async def start_handler(message: Message, state: FSMContext) -> None:
    try:
        await bot.send_chat_action(chat_id=message.chat.id, action="typing")
        text = markdown.text(
            f"Привет, {message.from_user.first_name}",
            sep='\n'
        )
        await message.answer(text=text, disable_web_page_preview=True)
        await state.set_state(Filtration.Main)
    except Exception as e:
        logger.exception("Ошибка в методе start_handler()", error=str(e))
