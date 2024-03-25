from datetime import datetime
from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from aiogram.types import Message


def offece_hours() -> bool:
    return datetime.now().weekday() in (
        0, 1, 2, 3, 4
        ) and datetime.now().hour in [
            i for i in range(8, 20)
            ]



class OfficeHoursMiddleware(BaseMiddleware):
    async def __call__(
            self, 
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], 
            event: Message, 
            data: Dict[str, Any]
            ) -> Any:
        if offece_hours():
            return await handler(event, data)
        
        await event.answer('Время работы бота: \r\nПн-пт с 8 до 20. Приходите в рабочие часы.')
        
