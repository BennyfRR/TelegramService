from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from consts.commands import TEST_COMMAND, TEST_COMMAND_TEXT
from consts.text import TEST_START_TEXT, TEST_NO_CONFIRM, RESULT, RESTART
from keyboards.survey_kb import *
from repositories.human_answers import HumansAnswersRepository
from repositories.question import QuestionRepository
from repositories.weight import WeightRepository


router = Router()


@router.message(Command(TEST_COMMAND))
async def test_command(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAIFV2ZKkH2BIxw'
                                     'AASc26ytyNiu3XQtxkQACAtoxGwgfWEodYZ33f7IFqAEAAwIAA3kAAzUE',
                               caption=TEST_START_TEXT, reply_markup=confirm_kb)


@router.callback_query(F.data.startswith("confirm_"))
async def confirm(call: CallbackQuery):
    action = call.data.split("_")[1]
    if action == "yes":
        questions = list(await QuestionRepository.all())
        question = questions[0]
        await call.message.answer(question.text, reply_markup=await get_question_kb(question.pk, 0))
    else:
        await call.message.answer(TEST_NO_CONFIRM, reply_markup=confirm_kb)


@router.callback_query(F.data.startswith("question_"))
async def question(call: CallbackQuery):
    pk, ind = map(int, call.data.split("_")[1:])
    questions = list(await QuestionRepository.all())
    pmi, mat, fun, pid, pri = list(map(float, (await WeightRepository.get_by_answer_id(ind)).weights.split(';')))
    ans = (await HumansAnswersRepository.get(pk=int(call.from_user.id)))
    if ans:
        weights = ans.weights
        old_pmi, old_mat, old_fun, old_pid, old_pri = list(map(float, weights.split(';')))
        pmi += old_pmi
        pri += old_pri
        mat += old_mat
        fun += old_fun
        pid += old_pid
        await HumansAnswersRepository.update(
            pk=call.from_user.id,
            weights=';'.join(map(str, [pmi, mat, fun, pid, pri]))
        )
    else:
        await HumansAnswersRepository.create(
            pk=call.from_user.id,
            weights=';'.join(map(str, [pmi, mat, fun, pid, pri]))
        )
    if pk + 1 < len(list(questions)):
        await call.message.answer(questions[pk + 1].text, reply_markup=await get_question_kb(questions[pk + 1].pk, pk + 1))
        await call.message.delete()
    else:
        max_weight = 0
        speciality = ''
        weights_dict = {
            '01.03.02 Прикладная математика и информатика': pmi,
            '02.03.03 Математическое обеспечение и администратирование информационных систем': mat,
            '02.03.02 Фундаментальная информатика и информационные технологии (Интеллектуальные системы и технологии) ': fun,
            '09.03.03 Информационные системы и технологии (Искусственный интеллект и машинное обучение)': pid,
            '09.03.04 Программная инженерия': pri
        }
        for x in weights_dict:
            if weights_dict[x] > max_weight:
                max_weight = weights_dict[x]
                speciality = x
        await call.message.answer(RESULT.format(speciality=speciality), reply_markup=another_time_kb)
        await call.message.delete()


@router.callback_query(F.data.startswith('restart_'))
async def restart(call: CallbackQuery):
    data = F.data.split('_')[1]
    if data == 'yes':
        questions = list(await QuestionRepository.all())
        question = questions[0]
        await call.message.answer(question.text, reply_markup=await get_question_kb(question.pk, 0))
        await call.message.delete()
