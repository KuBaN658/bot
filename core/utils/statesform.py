from aiogram.fsm.state import StatesGroup, State


class StepsForm(StatesGroup):
    get_name = State()
    get_last_name = State()
    get_age = State()