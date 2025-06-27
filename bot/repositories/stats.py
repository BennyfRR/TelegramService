from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from repositories.base import BaseRepository
from models.alchemy import StatsData


class StatsDataRepository(BaseRepository):
    model = StatsData

    @classmethod
    @BaseRepository.async_session
    async def get_by_department(cls, department: str, session: AsyncSession):
        return (await session.execute(select(
            cls.model.year, cls.model.score, cls.model.slots
        ).where(department == cls.model.department))).all()
