import io

from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message, InputFile, BufferedInputFile
import matplotlib.pyplot as plt

from consts.commands import GRADES_SCORES
from consts.text import CHOOSE_DEP_FOR_GRADE_STATS
from keyboards.stat_kb import stats_kb
from repositories.stats import StatsDataRepository


router = Router()


@router.message(Command(GRADES_SCORES))
async def grade_scores(msg: Message):
    await msg.answer(text=CHOOSE_DEP_FOR_GRADE_STATS, reply_markup=stats_kb)


@router.callback_query(F.data.startswith("stats_"))
async def stats(call: CallbackQuery):
    _, dep = call.data.split("_")
    res = await StatsDataRepository.get_by_department(department=dep)
    years, scores, slots = zip(*res)
    years = list(years)
    scores = list(scores)
    slots = list(slots)
    ans = ''
    for i in range(len(years)):
        ans += f'{years[i]}: {slots[i]}, '
    buf = io.BytesIO()
    plt.plot(years, scores, marker='o')
    plt.xticks(years)
    plt.xlabel("Год")
    plt.ylabel("Балл")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(buf, format='png', dpi=600)
    plt.close()
    buf.seek(0)
    photo = BufferedInputFile(buf.getvalue(), "graph.png")
    await call.message.answer_photo(photo, caption=f"Кол-во бюджетных мест по годам {ans}")
