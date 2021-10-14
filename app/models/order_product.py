from app.configs.database import db
from sqlalchemy import Column, Integer

order_product = db.Table('orders_products',
    Column('id', Integer, primary_key=True),
    Column('order_id', Integer, db.ForeignKey('orders.id')),
    Column('product_id', Integer, db.ForeignKey('products.id'))
)
