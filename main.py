import asyncio
import logging
import sys
from aiogram import F
from aiogram import Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import ContentType
from core.settings import settings

from bot import dp, bot
from core.filters.iscontact import IsTrueContact
from core.handlers.contact import get_true_contact, get_false_contact
from core.utils.commands import set_commands
from core.settings import settings
from core.handlers.basic import (
    get_photo, 
    get_hello, 
    get_start, 
    get_location, 
    get_inline
    )
from core.handlers.callback import select_macbook
from core.utils.callbackdata import MacInfo
from core.handlers.pay import (
    order,
    pre_checkout_query,
    successful_payment,
    shipping_check
    )
from core.middlewares.countermiddleware import CounterMiddleware
from core.middlewares.officehours import OfficeHoursMiddleware
from core.middlewares.dbmiddleware import DbSession
import asyncpg


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
    pool_connect = await asyncpg.create_pool(
        user='postgres', 
        password=settings.bots.password,
        database='users',
        host='127.0.0.1',
        port=5432,
        command_timeout=60
        )
    dp.update.middleware.register(DbSession(pool_connect))
    dp.message.middleware.register(CounterMiddleware())
    dp.message.middleware.register(OfficeHoursMiddleware())
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(order, Command(commands='pay'))
    dp.pre_checkout_query.register(pre_checkout_query)
    dp.message.register(successful_payment,F.successful_payment)
    dp.shipping_query.register(shipping_check)
    dp.message.register(get_inline, Command(commands='inline'))
    dp.callback_query.register(select_macbook, MacInfo.filter(F.chip == 'M1'))
    # dp.callback_query.register(select_macbook, F.data.startswith('apple_'))
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
    