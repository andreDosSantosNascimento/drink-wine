from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import backref, relationship


@dataclass
class Invoice(db.Model):
    __tablename__ = 'invoices'

    id = Column(Integer, primary_key=True)
    release_date = Column(Date, nullable=False,)
    invoice_number = Column(String(100), unique=True)
    order_id = Column(Integer, ForeignKey('orders.id'), unique=True)

    order = relationship('orders', backref=backref('invoices', uselist=False))
