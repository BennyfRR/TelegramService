from contextlib import asynccontextmanager

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from config.conf import ALCHEMY_CONNECTION_STRING


convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    'ix': 'ix__%(table_name)s__%(all_column_names)s',
    'uq': 'uq__%(table_name)s__%(all_column_names)s',
    'ck': 'ck__%(table_name)s__%(constraint_name)s',
    'fk': (
        'fk__%(table_name)s__%(all_column_names)s__'
        '%(referred_table_name)s'
    ),
    'pk': 'pk__%(table_name)s'
}

# Registry for all tables
metadata = MetaData(naming_convention=convention)


async_engine = create_async_engine(ALCHEMY_CONNECTION_STRING)
AsyncSessionFactory = async_sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)


@asynccontextmanager
async def get_async_session() -> AsyncSession:
    async with AsyncSessionFactory() as session:
        yield session
