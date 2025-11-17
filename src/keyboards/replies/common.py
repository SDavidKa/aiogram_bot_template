from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def get_request_contact_markup() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(
        text="Поделиться контактом",
        request_contact=True,
    )

    return builder.as_markup(resize_keyboard=True)
