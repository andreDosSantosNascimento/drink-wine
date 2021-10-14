from flask import Flask
from flask_migrate import Migrate


def init_app(app: Flask):
    Migrate(app, app.db)

    from app.models.product_model import Product
    from app.models.provider_model import Provider
    from app.models.provider_product import provider_product
    from app.models.order_model import Order
    from app.models.order_product import order_product
    from app.models.client_model import Client
    from app.models.invoices_model import Invoice
    from app.models.city_model import City
    from app.models.state_model import State
    from app.models.country_model import Country

