from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import backref, relationship


@dataclass
class City(db.Model):
    id: int
    ddd: str
    id_state:int

    __tablename__ = 'citys'

    id = Column(Integer, primary_key=True)
    ddd = Column(Integer, nullable=False, unique=True)
    id_state = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('State', backref=backref('city', uselist=False))
