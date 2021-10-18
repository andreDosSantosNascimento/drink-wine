from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class Client(db.Model):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False,)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(100), unique=True)
    cnpj = Column(String(100), nullable=False, unique=True)
    city_id = Column(Integer, ForeignKey('citys.id'), nullable=False)

    city = relationship('City', backref=backref('client', uselist=False))
