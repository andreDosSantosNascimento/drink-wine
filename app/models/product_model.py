from dataclasses import dataclass
from datetime import datetime

from app.configs.database import db
from app.models.errors_product import InvalidOrderDateError, InvalidValueuError
from app.models.provider_product import provider_product
from sqlalchemy import Column, Date, Float, Integer, String
from sqlalchemy.orm import validates


@dataclass
class Product(db.Model):
    id: str
    name: str
    value: int
    description: str
    expiration_date: Date

    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)
    value = Column(Float, nullable=False)
    description = Column(String(255))
    expiration_date = Column(Date, nullable=False)

    provider = db.relationship('Provider', secondary=provider_product,
                            backref=db.backref('products', uselist=True))


    @validates('name','value','expiration_date')
    def validate_types(self, key, value):

        if key == 'name':
            value = value.upper()

        if key == 'value' and type(value) is not float or not int:
            raise InvalidValueuError

        if key == 'expiration_date':
            try:
                datetime.strptime(value, '%Y/%m/%d')
            except:
                raise InvalidOrderDateError
        return value
