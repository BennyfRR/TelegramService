from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


stats_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Прикладная Математика и Информатика", callback_data='stats_pmi')
        ],
        [
            InlineKeyboardButton(text="Математическое обеспечение и администрирование информационных систем", callback_data='stats_moais')
        ],
        [
            InlineKeyboardButton(text="Фундаментальная информатика и информационные технологии", callback_data='stats_fund')
        ],
        [
            InlineKeyboardButton(text="Прикладная информатика", callback_data='stats_pi')
        ],
        [
            InlineKeyboardButton(text="Программная инженерия", callback_data='stats_pri')
        ]
    ]
)