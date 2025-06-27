from sqlalchemy import select, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from models.alchemy import Weight
from repositories.base import BaseRepository


class WeightRepository(BaseRepository):
    model = Weight

    @classmethod
    @BaseRepository.async_session
    async def get_by_answer_id(cls, question_id: int, session: AsyncSession) -> ScalarResult[model] | None:
        stmt = select(cls.model).where(cls.model.answer_id == question_id)
        res = await session.execute(stmt)
        return res.scalar_one_or_none()
