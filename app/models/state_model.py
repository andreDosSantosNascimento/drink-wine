from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class State(db.Model):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    sigla = Column(String(3), nullable=False)
    id_country = Column(Integer, ForeignKey('countrys.id'), nullable=False)

    country = relationship('countrys', backref=backref('state', uselist=False))
