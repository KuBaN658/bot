from contextlib import suppress
from aiogram.filters import Command
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot
from aiogram import F
from aiogram.exceptions import TelegramBadRequest
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from random import randint

from bot import dp, bot


@dp.message(F.text == "Прораммист")
async def send_programmer(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Web Developer"), 
         types.KeyboardButton(text="Mobile Developer"),
         types.KeyboardButton(text="Data Scientist")
        ]
    ]
    keyboard = types.ReplyKeyboardMarkup(
            keyboard=kb, 
            resize_keyboard=True, 
            input_field_placeholder="Или предложите свой вариант"
            )
    await message.answer("В каком направлении?", reply_markup=keyboard)


@dp.message(F.text == "Другое")
async def send_other(message: types.Message):
    await message.answer('Введите свой вариант ответа')

@dp.message(Command("inline_url"))
async def cmd_inline_url(message: types.Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="GitHub", url="https://github.com")
        )

    builder.row(types.InlineKeyboardButton(
        text="Оф. канал Telegram",
        url="tg://resolve?domain=telegram")
        )
    
    user_id = 1489510945
    chat_info = await bot.get_chat(user_id)
    if not chat_info.has_private_forwards:
        builder.row(
        types.InlineKeyboardButton(
            text="Какой-то пользователь",
            url=f"tg://user?id={user_id}")
            )

    await message.answer(
        'Выберите ссылку', reply_markup=builder.as_markup(),
    )

@dp.message(Command("random"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    with suppress(TelegramBadRequest):
        await message.answer(
            "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
            reply_markup=builder.as_markup()
        )

@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))
    await callback.answer()

@dp.message(Command("reply_builder"))
async def reply_builder(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 17):
        builder.add(types.KeyboardButton(text=str(i)))
        builder.adjust(4)
    await message.answer( 
        "Выберите число:", 
        reply_markup=builder.as_markup(resize_keyboard=True), 
    )

@dp.message(Command('get_my_id'))
async def get_my_id(message: types.Message):
    user_id = message.from_user.id
    await message.answer(f"Ваш user_id: {user_id}")

@dp.message(Command("sticker"))
async def cmd_inline_url(message: types.Message, bot: Bot):
    await bot.send_sticker(
        chat_id=message.from_user.id,
        sticker='CAACAgIAAxkBAAEKylVlXGJiYeK0IauZl0oifvrrjsgu3AACZAADWbv8JToS9CchlsxoMwQ'
    )

@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer('Технические шоколадки!')
