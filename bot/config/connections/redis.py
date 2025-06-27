from redis.asyncio.client import Redis

from config.conf import REDIS_CONNECTION_STRING


redis_client = Redis.from_url(REDIS_CONNECTION_STRING)
