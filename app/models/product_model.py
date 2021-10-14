from dataclasses import dataclass

from app.configs.database import db
from app.models.provider_product import provider_product
from sqlalchemy import Column, Date, Float, Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False,)
    value = Column(Float, nullable=False)
    description = Column(String(255))
    expiration_date = Column(Date, nullable=False)

    provider = relationship('providers', secondary=provider_product,
                            backref=backref('products', uselist=True))
