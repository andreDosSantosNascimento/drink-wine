from dataclasses import dataclass
from sqlalchemy.orm import validates

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship

from app.models.error_model import InvalidError, InvalidEmailError, WrongNumberFormatError, WrongTypeError


@dataclass
class Provider(db.Model):

    id: int
    name: str
    email: str
    phone: str
    country_id: int
    nif: str

    __tablename__ = 'providers'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False,)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String(100), unique=True)
    country = db.relationship('Country', backref=db.backref('providers'))
    country_id = Column(Integer, ForeignKey('countrys.id'), nullable=False)
    nif = Column(String(9), nullable=False, unique=True)

    @validates("name","email", "phone", "nif")
    def validate_types(self, key, value):
        
        if type(value) != str:
            raise WrongTypeError(key, "string")

        if key == "name":
            value = value.title()
        
        if key == "nif" and not value.isnumeric():
            raise InvalidError("nif")

        if key == "phone" and not value.isnumeric():
            raise WrongNumberFormatError
        
        if key == "email" and not "@" in value:
            raise InvalidEmailError

        return value
