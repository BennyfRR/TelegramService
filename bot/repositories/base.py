from typing import Any

from sqlalchemy import select, ScalarResult
from sqlalchemy.ext.asyncio import AsyncSession

from config.connections.alchemy import get_async_session
from models.alchemy import Model


class BaseRepository:
    model = None

    @staticmethod
    def async_session(func):
        async def wrapper(*args, **kwargs):
            async with get_async_session() as session:
                kwargs['session'] = session
                res = await func(*args, **kwargs)
                await session.commit()
            return res
        return wrapper

    @classmethod
    @async_session
    async def get(cls, pk: int, session: AsyncSession) -> ScalarResult[model]:
        stmt = select(cls.model).where(cls.model.pk == pk)
        res = await session.execute(stmt)
        return res.scalar()

    @classmethod
    @async_session
    async def all(cls, session: AsyncSession) -> ScalarResult[Any]:
        stmt = select(cls.model)
        res = await session.execute(stmt)
        return res.scalars()

    @classmethod
    @async_session
    async def update(cls, pk: int, session: AsyncSession, **kwargs):
        kwargs.pop('session', None)
        stmt = select(cls.model).where(cls.model.pk == pk)
        res = await session.execute(stmt)
        mdl = res.scalar_one()
        for key, value in kwargs.items():
            setattr(mdl, key, value)

    @classmethod
    @async_session
    async def create(cls, session: AsyncSession, **kwargs) -> ScalarResult[model]:
        ins = cls.model(**kwargs)
        session.add(ins)
        await session.commit()
        return ins

    @classmethod
    @async_session
    async def destroy(cls, pk: int, session: AsyncSession) -> ScalarResult[model] | None:
        ins = await session.get(cls.model, pk)
        if ins:
            await session.delete(ins)
            await session.commit()
            return ins
        return
