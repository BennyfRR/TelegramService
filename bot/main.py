import logging

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage
from dotenv import load_dotenv

from config import conf
from config.connections.redis import redis_client
from consts.commands import COMMANDS_LIST
from handlers import survey, university, admin, stats


load_dotenv()


async def on_startup(dp):
    pass


async def on_shutdown(dp):
    await dp.storage.close()
    await dp.storage.wait_closed()


async def main() -> None:
    storage = RedisStorage(redis_client)
    bot = Bot(token=conf.BOT_TOKEN, )
    dp = Dispatcher(bot=bot, storage=storage)
    dp.include_routers(survey.router, university.router, admin.router, stats.router)
    await bot.delete_webhook()
    await bot.set_my_commands(COMMANDS_LIST)
    await dp.start_polling(bot, on_startup=on_startup, on_shutdown=on_shutdown)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
