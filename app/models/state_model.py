from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class State(db.Model):
    id: int
    sigla: str
    id_country: int

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    sigla = Column(String(2), nullable=False, unique=True)
    country = db.relationship('Country', 
                              backref=db.backref('state', uselist=False))
    id_country = Column(Integer, ForeignKey('countrys.id'), nullable=False)
