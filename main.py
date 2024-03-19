import asyncio
import logging
import sys
from aiogram import F
from aiogram import Bot
from aiogram.filters import CommandStart
from aiogram.types import ContentType

from bot import dp, bot
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_true_contact, get_false_contact
from core.utils.commands import set_commands
from core.settings import settings
from core.handlers.basic import get_photo, get_hello, get_start, get_location


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(settings.bots.admin_id, text='Бот остановлен!')


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s"
               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, CommandStart())
    dp.message.register(get_location, F.location)
    dp.message.register(get_hello, F.text == 'Привет')
    dp.message.register(get_true_contact, F.contact, IsTrueContact())
    dp.message.register(get_false_contact, F.contact)
    dp.message.register(get_photo, F.photo)
    
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())