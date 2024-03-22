from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from core.utils.callbackdata import MacInfo


select_macbook = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Macbook Air 13 M1 2020',
                callback_data='apple_air_13_m1_2020'
            )
        ],
        [
            InlineKeyboardButton(
                text='Macbook Pro 14 M2 2021',
                callback_data='apple_air_14_m1_2021'
            )
        ],
        [
            InlineKeyboardButton(
                text='Macbook Super 15 M3 2022',
                callback_data='apple_air_15_m1_2022'
            )
        ],
        [
            InlineKeyboardButton(
                text='Link',
                url='https://mail.ru/'
            )
        ],
        [
            InlineKeyboardButton(
                text='Profile',
                url='https://t.me/KuBaN_123'
            )
        ],
    ]
)


def get_inline_keyboard():
    keyboard_builder = InlineKeyboardBuilder()
    keyboard_builder.button(
        text='Macbook Air 13 M1 2020',
        callback_data=MacInfo(
            model='air',
            size=13,
            chip='M1',
            year=2020
        )
    )
    keyboard_builder.button(
        text='Macbook Pro 14 M2 2021',
        callback_data=MacInfo(
            model='pro',
            size=14,
            chip='M1',
            year=2021
        )
    )
    keyboard_builder.button(
        text='Macbook Super 15 M3 2022',
        callback_data=MacInfo(
            model='super',
            size=15,
            chip='M1',
            year=2023
        )
    )
    keyboard_builder.button(
        text='Link',
        url='https://mail.ru/'
    )
    keyboard_builder.button(
        text='Profile',
        url='https://t.me/KuBaN_123'
    )
    keyboard_builder.adjust(3, 1, 1)
    return keyboard_builder.as_markup()
