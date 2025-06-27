from models.alchemy import HumanAnswer
from repositories.base import BaseRepository


class HumansAnswersRepository(BaseRepository):
    model = HumanAnswer
