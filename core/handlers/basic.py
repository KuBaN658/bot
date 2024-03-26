import json
from bot import dp
from aiogram import Bot, F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart
from core.keyboards.reply import reply_keyboard, loc_tel_poll_keyboard, get_reply_keyboard
from core.keyboards.inline import select_macbook, get_inline_keyboard
from core.utils.dbconnect import Request


async def get_inline(message: Message, bot: Bot):
    await message.answer(
        f'Привет, {message.from_user.first_name}. Показываю инлайн кнопки!',
        reply_markup=get_inline_keyboard()
        )


async def get_start(message: Message, bot: Bot, counter: str, request: Request):
    await request.add_data(message.from_user.id, message.from_user.first_name)
    await message.answer(f'Сообщение #{counter}')
    await message.answer(
        f'Привет, <b>{message.from_user.first_name}</> рад тебя видеть!',
        reply_markup=get_reply_keyboard()
        )
    

async def get_location(message: Message, bot: Bot):
    await message.answer(
        f'Ты отправил локацию!\r\a'
        f'{message.location.latitude}\r\n{message.location.longitude}'
        )


async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично ты отправил картинку, я сохраню ее.')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path, 'photo.jpg')


async def get_hello(message: Message, bot: Bot):
    await message.answer('И тебе привет!!!')
    print(message.model_dump_json())
    