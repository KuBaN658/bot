from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from core.utils.statesform import StepsForm

async def get_form(message: Message, state: FSMContext):
    await message.answer(f'{message.from_user.first_name}, начинаем заполнять анкету. Введите свое имя')
    await state.set_state(StepsForm.get_name)


async def get_name(message: Message, state: FSMContext):
    await message.answer(f'Твоё имя: \r\n{message.text}\r\nТеперь введите фамилию')
    await state.update_data(name=message.text)
    await state.set_state(StepsForm.get_last_name)


async def get_last_name(message: Message, state: FSMContext):
    await message.answer(f'Твоя фамилия: \r\n{message.text}\r\nТеперь введите возраст')
    await state.update_data(last_name=message.text)
    await state.set_state(StepsForm.get_age)


async def get_age(message: Message, state: FSMContext):
    await message.answer(f'Твой возраст: \r\n{message.text}\r\n')
    context_data = await state.get_data()
    await state.set_state(StepsForm.get_age)
    await message.answer(f'Сохраненные данные в машине состояний: \r\n{str(context_data)}')
    name = context_data.get('name')
    last_name = context_data.get('last_name')
    data_user = f'Вот твои данные\r\n' \
                f'Имя: {name}\r\n' \
                f'Фамилия: {last_name}\r\n' \
                f'Возраст: {message.text}'
    await message.answer(data_user)
    await state.clear()
