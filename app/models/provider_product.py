from app.configs.database import db
from sqlalchemy import Column, Integer

provider_product = db.Table('providers_products',
    Column('id',Integer, primary_key=True),
    Column('provider_id', Integer, db.ForeignKey('providers.id')),
    Column('product_id', Integer, db.ForeignKey('products.id'))
)
