from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import backref, relationship


@dataclass
class City(db.Model):
    __tablename__ = 'citys'

    id = Column(Integer, primary_key=True)
    ddd = Column(Integer)
    id_state = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('states', backref=backref('city', uselist=False))
