from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from consts.text import START_TEXT, FACULTY_ABOUT, DEPARTMENT_INFO
from consts.commands import START_COMMAND, FPM_ABOUT_COMMAND, DEPARTMENT_COMMAND, DEK_COM, FACULTY_COM
from keyboards.survey_kb import department, main_kb, dekanat_kb, facul_site
from consts.text import DEPARTMENTS, DEK, FACULTY
from utils.long_message import long_message_control

router = Router()


@router.message(Command(START_COMMAND))
async def start(msg: Message):
    await msg.answer_photo(photo='AgACAgIAAxkBAAIE62ZKgsEvrLiSRKF4_UVSZ5QVwFKfAAKW4jEbCB9QSuTXK9ILplbEAQADAgADbQADNQQ',
                           caption=START_TEXT.format(username=msg.from_user.username), reply_markup=main_kb)


@router.message(F.photo)
async def get_photo(msg: Message):
    await msg.answer(f'ID фото: {msg.photo[-1].file_id}')


@router.message(Command(DEPARTMENT_COMMAND))
async def dep(msg: Message):
    await msg.answer_photo(photo='AgACAgIAAxkBAAIEwGZKelCJlqgHsrTxzWd2qDc'
                                 '-AhxJAAKJ4jEbCB9QStU8tHDBz-1rAQADAgADbQADNQQ',
                           caption=DEPARTMENT_INFO, reply_markup=department)


@router.callback_query(F.data.startswith("dep_"))
async def choice(call: CallbackQuery):
    chs = call.data.split("_")[1]
    if chs == "kit":
        await call.message.answer_photo(photo='AgACAgIAAxkBAAIFKWZKi1fjNi3ysDlXxPnkFNAAAS72gAAC-dkxGwgfWEqMEJNEnfFW'
                                              '-QEAAwIAA3kAAzUE',
                                        caption=DEPARTMENTS[0])
    if chs == "kvt":
        await call.message.answer_photo(photo='AgACAgIAAxkBAAIFMWZKjEK5dJOcMgrcaymHQpPN_iqaAAL62TEbCB9YSvBCUWhQuY'
                                              '9XAQADAgADeQADNQQ',
                                        caption=DEPARTMENTS[1])
    if chs == "kmm":
        await call.message.answer_photo(photo='AgACAgIAAxkBAAIFNGZKjItLIRqfOeAc6NHHh'
                                              'HkkYDyeAAL72TEbCB9YSjASwzmAbBMrAQADAgADeQADNQQ',
                                        caption=DEPARTMENTS[2])
    if chs == "kadii":
        await call.message.answer_photo(photo='AgACAgIAAxkBAAIFOmZKjNa8rO0AAZlo'
                                              'cFAt1gkOgFE-1wAC_NkxGwgfWEoyW2bjiUjjxgEAAwIAA3kAAzUE',
                                        caption=DEPARTMENTS[3])
    if chs == "kpm":
        await call.message.answer_photo(photo='AgACAgIAAxkBAAIFPWZKjWniX9iIyikmvQxoP0Td_SS'
                                              '0AAL92TEbCB9YSnwEpwbioVi-AQADAgADeQADNQQ',
                                        caption=DEPARTMENTS[4])


@router.message(Command(FPM_ABOUT_COMMAND))
async def fpm_history(msg: Message):
    await msg.answer_photo(photo='AgACAgIAAxkBAAIH62hCgQcAAeuuDOjOr7S-Zo9DvchgVQAC2fgxG-JmEEqA4KvfpOMPcgEAAwIAA3gAAzYE',
                            caption=FACULTY_ABOUT)


@router.message(Command(FACULTY_COM))
async def facul(msg: Message):
        await msg.answer_photo(photo='AgACAgIAAxkBAAIGRmZK5ndvGdW2zSh9SHtZ3vc6jlxXAA'
                                     'Jd4DEbEuZZSmGVDj3aeawcAQADAgADeQADNQQ',
                               caption=FACULTY, reply_markup=facul_site)


@router.message(Command(DEK_COM))
async def dek1(msg: Message):
    await msg.answer_photo(photo='AgACAgIAAxkBAAIGHGZK2SwvruH7jz'
                                     'c7CS6shTAPTVtiAAI55TEbEuZRSiwDkoxvjvJTAQADAgADeQADNQQ',
                           caption=DEK, reply_markup=dekanat_kb)


@router.message(F.text.lower().in_(["страница деканата", "сайт факультета"]))
async def echo(msg: Message):
    message = msg.text.lower()
    if message == "страница деканата":
        await msg.answer_photo(photo='AgACAgIAAxkBAAIGHGZK2SwvruH7jz'
                                     'c7CS6shTAPTVtiAAI55TEbEuZRSiwDkoxvjvJTAQADAgADeQADNQQ',
                               caption=DEK, reply_markup=dekanat_kb)
    if message == "сайт факультета":
        await msg.answer_photo(photo='AgACAgIAAxkBAAIGRmZK5ndvGdW2zSh9SHtZ3vc6jlxXAA'
                                     'Jd4DEbEuZZSmGVDj3aeawcAQADAgADeQADNQQ',
                               caption=FACULTY, reply_markup=facul_site)
