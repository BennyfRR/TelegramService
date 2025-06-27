from aiogram.filters.state import State, StatesGroup


class AddStats(StatesGroup):
    waiting_for_department = State()
    waiting_for_score = State()
    waiting_for_year = State()
    waiting_for_slots = State()
