from sqlalchemy import *
from sqlalchemy.orm import DeclarativeBase


class Model(DeclarativeBase):
    pass


class Admin(Model):
    __tablename__ = 'admins'
    pk = Column(BigInteger, primary_key=True, index=True)


class Question(Model):
    __tablename__ = 'questions'
    pk = Column(BigInteger, primary_key=True, index=True)
    text = Column(Text)


class Answer(Model):
    __tablename__ = 'answers'
    pk = Column(BigInteger, primary_key=True, index=True)
    text = Column(Text)
    question_id = Column(BigInteger, ForeignKey('questions.pk', ondelete='CASCADE'), nullable=False, index=True)


class Weight(Model):
    __tablename__ = 'weights'
    pk = Column(BigInteger, primary_key=True, index=True)
    answer_id = Column(BigInteger, ForeignKey('answers.pk', ondelete='CASCADE'), index=True)
    weights = Column(Text)


class HumanAnswer(Model):
    __tablename__ = 'human_answers'
    pk = Column(BigInteger, primary_key=True, index=True)
    speciality = Column(Text)
    weights = Column(Text)


class StatsData(Model):
    __tablename__ = 'stats_data'
    pk = Column(BigInteger, primary_key=True, index=True)
    department = Column(Text)
    score = Column(Integer)
    year = Column(Integer)
    slots = Column(Integer)
