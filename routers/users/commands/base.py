from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown

from states.user import Menu

router = Router(name=__name__)


@router.message(CommandStart())
async def start(message: types.Message, state: FSMContext) -> None:
    await state.set_state(Menu.start)
    await state.update_data(data={"telegram_name": f'{message.from_user.first_name} {message.from_user.last_name}'})
    text = markdown.text(
        markdown.text("Привет, это БОТ ✋"),
        sep="\n\n",
    )

    await message.answer(text=text)
