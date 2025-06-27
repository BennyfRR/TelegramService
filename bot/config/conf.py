from os import getenv

from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = getenv('BOT_TOKEN')
ADMINISTRATORS = list(map(int, getenv('ADMINS').split(',')))
REDIS_CONNECTION_STRING = getenv('REDIS_URL')
ALCHEMY_CONNECTION_STRING = getenv("ALCHEMY_ENGINE")
