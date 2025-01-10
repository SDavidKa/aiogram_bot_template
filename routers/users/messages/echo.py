from aiogram import types, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

router = Router(name=__name__)


@router.message()
async def start(message: types.Message, state: FSMContext) -> None:
    await message.reply('Я не знаю такую команду, для начала работы нажми на команду /start', reply_markup=ReplyKeyboardRemove())
    await state.set_data(data={"telegram_name": f'{message.from_user.first_name} {message.from_user.last_name}'})
