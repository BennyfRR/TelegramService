from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

from repositories.answer import AnswerRepository


confirm_kb = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text='Подтверждаю', callback_data='confirm_yes', )
        ],
        [
            InlineKeyboardButton(text='Не подтверждаю', callback_data='confirm_no'),
        ]
    ]
)


async def get_question_kb(question_id, ind):
    answers = list(await AnswerRepository.get_by_question_id(question_id=question_id))

    # Каждый ответ — отдельный ряд (вложенный список)
    keyboard = [
        [InlineKeyboardButton(text=f'{answer.text}', callback_data=f'question_{ind}_{answer.pk}')]
        for answer in answers
    ]

    return InlineKeyboardMarkup(inline_keyboard=keyboard)

another_time_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Пройти заново', callback_data='restart_yes'),
        ]
    ]
)

department = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="КИТ", callback_data='dep_kit')
        ],
        [
            InlineKeyboardButton(text="КВТ", callback_data='dep_kvt'),
        ],
        [
            InlineKeyboardButton(text="КММ", callback_data='dep_kmm'),
        ],
        [
            InlineKeyboardButton(text="КАДИИ", callback_data='dep_kadii')
        ],
        [
            InlineKeyboardButton(text="КПМ", callback_data='dep_kpm')
        ]
    ]
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Сайт факультета"),
            KeyboardButton(text="Страница деканата")
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите действие из меню",
    selective=True
)

dekanat_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="Cтраница деканата", url="https://vk.com/fctandam")
        ],
    ],
)

facul_site = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="Cайт факультета", url="https://www.kubsu.ru/ru/fktipm")
        ],
    ],
)