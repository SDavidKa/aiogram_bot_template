from enum import Enum

from aiogram.types import InlineKeyboardMarkup, WebAppInfo
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Пример
class FilterType(str, Enum):
    by_types = "Критерии групп"
    by_subway = "Метро/Электрички"


class FilterTypeData(CallbackData, prefix="filter"):
    filter_type: str


def get_filter_type_markup() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()

    for filter_type in FilterType:
        builder.button(
            text=filter_type.value,
            callback_data=FilterTypeData(filter_type=filter_type.name).pack()
        )

    builder.adjust(1)
    return builder.as_markup()

