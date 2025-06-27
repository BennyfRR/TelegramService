from sqlalchemy import select, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from models.alchemy import Answer
from repositories.base import BaseRepository


class AnswerRepository(BaseRepository):
    model = Answer

    @classmethod
    @BaseRepository.async_session
    async def get_by_question_id(cls, question_id: int, session: AsyncSession) -> ScalarResult[model]:
        stmt = select(cls.model).where(cls.model.question_id == question_id)
        res = await session.execute(stmt)
        return res.scalars()
