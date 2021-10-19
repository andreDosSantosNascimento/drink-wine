from dataclasses import dataclass

from app.configs.database import db
from app.models.order_product import order_product
from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import backref, relationship
from datetime import datetime


@dataclass
class Order(db.Model):

    id: int
    order_date: datetime
    provider_id: int
    client_id: int
    products: list

    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    order_date = Column(Date, nullable=False,)
    provider_id = Column(Integer, ForeignKey('providers.id'), nullable=False)
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=False)

    products = relationship('Product', secondary=order_product,
                            backref=backref('orders', uselist=True))
