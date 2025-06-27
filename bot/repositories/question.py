from models.alchemy import Question
from repositories.base import BaseRepository


class QuestionRepository(BaseRepository):
    model = Question
