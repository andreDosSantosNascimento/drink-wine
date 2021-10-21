from dataclasses import dataclass

from app.configs.database import db

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship, validates

from app.models.error_model import InvalidEmailError, InvalidError, WrongNumberFormatError, WrongTypeError

@dataclass
class Client(db.Model):
    id:int
    name:str
    email:str
    phone:str
    cnpj:str
    
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False,)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(100), unique=True)
    cnpj = Column(String(100), nullable=False, unique=True)
    city_id = Column(Integer, ForeignKey('citys.id'), nullable=False)

    city = relationship('City', backref=backref('client', uselist=False))

    @validates("name","email", "phone", "cnpj")
    def validate_types(self, key, value):
        
        if type(value) != str:
            raise WrongTypeError(key, "string")

        if key == "name":
            value = value.title()
        
        if key == "cnpj" and len(value) != 14 and not value.isnumeric():
            raise InvalidError(key)

        if key == "phone" and not value.isnumeric():
            raise WrongNumberFormatError
        
        if key == "email" and not "@" in value:
            raise InvalidEmailError

        return value
