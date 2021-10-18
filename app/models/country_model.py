from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String


@dataclass
class Country(db.Model):
    id: int
    sigla: str
    ddd: str

    __tablename__ = 'countrys'

    id = Column(Integer, primary_key=True)
    sigla = Column(String(3), nullable=False, unique=True)
    ddd = Column(String(3))
