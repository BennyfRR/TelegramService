from models.alchemy import Admin
from repositories.base import BaseRepository


class AdminRepository(BaseRepository):
    model = Admin
