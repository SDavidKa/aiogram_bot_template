from aiogram.fsm.state import State, StatesGroup


class Menu(StatesGroup):
    terms = State()
    start = State()
    first_step = State()
    second_step = State()
    pre_payment = State()
    update_pay = State()
