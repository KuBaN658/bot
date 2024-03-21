from aiogram import Bot
from aiogram.types import Message, LabeledPrice, PreCheckoutQuery


async def order(message: Message, bot: Bot):
    await bot.send_invoice(
        chat_id=message.chat.id,
        title='Покупка через Telegram-бот',
        description='Учимся принимать платежи через Telegram бот',
        payload='Payment through a bot',
        provider_token= '381764678:TEST:80914',
        currency='rub',
        prices=[
            LabeledPrice(
                label='Доступ к секретной информации',
                amount=99000
            ),
            LabeledPrice(
                label='НДС',
                amount=20000
            ),
            LabeledPrice(
                label='Скидка',
                amount=-20000
            ),
            LabeledPrice(
                label='Бонус',
                amount=-40000
            )
            
        ],
        max_tip_amount=5000,  # максимальная сумма чаевых
        suggested_tip_amounts=[1000, 2000, 3000, 4000],  # варианты чаевых
        start_parameter='KuBaN',
        provider_data=None,
        photo_url=None,
        photo_size=100,
        photo_width=800,
        photo_height=450,
        need_name=True,
        need_phone_number=True,
        need_email=True,
        need_shipping_address=False,
        send_phone_number_to_provider=True,
        send_email_to_provider=True,
        is_flexible=False,
        disable_notification=False,
        protect_content=False,
        reply_to_message_id=None,
        allow_sending_without_reply=True,
        reply_markup=None,
        request_timeout=15,
    )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: Message):
    msg = f'Спасибо за оплату {message.successful_payment.total_amount // 100}' \
          f'{message.successful_payment.currency}.' \
          f'\r\nНаш менеджер получил заявку и уже набирает Ваш номер телефона.' \
          f'\r\nПока можете скачать цифровую версию нашего продукта https://github.com/KuBaN658'
    await message.answer(msg)