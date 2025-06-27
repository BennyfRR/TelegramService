import asyncio

import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    dbname='db',
    user='postgres',
    password='megasecretpassword',
    host='localhost',
    port=5432
)

with conn.cursor() as cursor:
    # req = sql.SQL("TRUNCATE TABLE questions CASCADE")
    # req = sql.SQL("TRUNCATE TABLE stats_data CASCADE")
    req = sql.SQL("SELECT * FROM stats_data;")

    cursor.execute(req)
    print(*cursor.fetchall(), sep='\n')
    conn.commit()

from repositories.stats import StatsDataRepository
async def a():
    res = await StatsDataRepository.get_by_department(department='pmi')
    print(res)


asyncio.run(a())
