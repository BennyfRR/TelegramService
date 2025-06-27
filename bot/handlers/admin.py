from aiogram import F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from consts.text import ADMIN_CREATED, ADMIN_TO_CREATE, QUESTION_TO_CREATE, ANSWER_TO_CREATE, WEIGHTS_TO_CREATE, QUESTION_CREATED, QUESTIONS_ADDED
from keyboards.admin import finish_add_questions_kb, finish_add_answers_kb
from middlewares.admin import AdminAuthorizationMiddleware
from repositories.admin import AdminRepository
from repositories.answer import AnswerRepository
from repositories.stats import StatsDataRepository
from repositories.question import QuestionRepository
from repositories.weight import WeightRepository
from states.admin import CreateAdminState
from states.stats import AddStats
from states.question import CreateQuestionState


router = Router()


@router.message(Command('add_admin'))
async def add_admin(message: Message, state: FSMContext):
    await message.answer(ADMIN_TO_CREATE)
    await state.set_state(CreateAdminState.waiting_for_admin_id)


@router.message(CreateAdminState.waiting_for_admin_id)
async def add_admin_id(message: Message, state: FSMContext):
    await AdminRepository.create(pk=int(message.text))
    await message.answer(ADMIN_CREATED.format(tg_id=message.text))
    await state.clear()


@router.message(Command('add_question'))
async def add_question(message: Message, state: FSMContext):
    await message.answer(QUESTION_TO_CREATE, reply_markup=finish_add_questions_kb)
    await state.set_state(CreateQuestionState.waiting_for_question_text)


@router.message(CreateQuestionState.waiting_for_question_text)
async def create_question(message: Message, state: FSMContext):
    await message.answer(ANSWER_TO_CREATE, reply_markup=finish_add_answers_kb)
    await state.update_data(
        question=message.text,
        answers=[]
    )
    await state.set_state(CreateQuestionState.waiting_for_answer_text)


@router.message(CreateQuestionState.waiting_for_answer_text)
async def add_answer(message: Message, state: FSMContext):
    data = await state.get_data()
    data['answers'].append([message.text])
    await message.answer(WEIGHTS_TO_CREATE)
    await state.update_data(answers=data['answers'])
    await state.set_state(CreateQuestionState.waiting_for_weights)


@router.message(CreateQuestionState.waiting_for_weights)
async def add_weights(message: Message, state: FSMContext):
    data = await state.get_data()
    data['answers'][-1].append(message.text)
    await state.update_data(answers=data['answers'])
    await message.answer(ANSWER_TO_CREATE, reply_markup=finish_add_answers_kb)
    await state.set_state(CreateQuestionState.waiting_for_answer_text)


@router.callback_query(F.data.startswith("add_answer_"))
async def add_answer_callback(call: CallbackQuery, state: FSMContext):
    if call.data.split('_')[-1] == 'finish':
        data = await state.get_data()
        try:
            if not data['answers']:
                raise KeyError
            question = await QuestionRepository.create(
                text=data['question']
            )
            for i in range(len(data['answers'])):
                answer = await AnswerRepository.create(question_id=question.pk, text=data['answers'][i][0])
                await WeightRepository.create(answer_id=answer.pk, weights=data['answers'][i][1])
            await state.update_data(answers=[])
            await call.message.answer(QUESTIONS_ADDED)
        except KeyError:
            pass
        await call.message.answer(QUESTION_TO_CREATE, reply_markup=finish_add_questions_kb)
        await state.set_state(CreateQuestionState.waiting_for_question_text)


@router.callback_query(F.data.startswith("add_question_"))
async def add_question_callback(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    if call.data.split('_')[-1] == 'finish':
        try:
            if not data['answers']:
                raise KeyError
            question = await QuestionRepository.create(
                text=data['question']
            )
            for i in range(len(data['answers'])):
                answer = await AnswerRepository.create(question_id=question.pk, text=data['answers'][i][0])
                await WeightRepository.create(answer_id=answer.pk, weights=data['answers'][i][1])
            await call.message.answer(QUESTIONS_ADDED)
        except KeyError:
            pass
        # finally:
        #     questions = await QuestionRepository.all()
        #     for question in questions:
        #         await QuestionRepository.destroy(question_text=question['question_text'])
        #     for i, question in enumerate(questions):
        #         await QuestionRepository.create(
        #             ind=i,
        #             question_text=question['question_text'],
        #             answers=question['answers']
        #         )
        await state.clear()


@router.message(Command('add_stats'))
async def cmd_add(message: Message, state: FSMContext):
    await state.set_state(AddStats.waiting_for_department)
    await message.answer("Введите код направления(pmi, moais, fund, pi, pri):")


@router.message(AddStats.waiting_for_department)
async def process_department(message: Message, state: FSMContext):
    await state.update_data(department=message.text)
    await state.set_state(AddStats.waiting_for_score)
    await message.answer("Введите количество баллов (целое число):")


@router.message(AddStats.waiting_for_score)
async def process_score(message: Message, state: FSMContext):
    try:
        score = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста, введите целое число.")
        return
    await state.update_data(score=score)
    await state.set_state(AddStats.waiting_for_year)
    await message.answer("Введите год (например, 2024):")


@router.message(AddStats.waiting_for_year)
async def process_year(message: Message, state: FSMContext):
    try:
        year = int(message.text)
    except ValueError:
        await message.answer("Введите корректный год.")
        return
    await state.update_data(year=year)
    await state.set_state(AddStats.waiting_for_slots)
    await message.answer("Введите кол-во бюджетных мест в этом году")


@router.message(AddStats.waiting_for_slots)
async def process_slots(message: Message, state: FSMContext):
    try:
        slots = int(message.text)
    except ValueError:
        await message.answer("Пожалуйста, введите целое число.")
        return

    data = await state.get_data()

    await StatsDataRepository.create(
        department=data['department'],
        score=data['score'],
        year=data['year'],
        slots=slots
    )

    await message.answer("Запись успешно добавлена ✅")
    await state.clear()


router.message.middleware(AdminAuthorizationMiddleware())
