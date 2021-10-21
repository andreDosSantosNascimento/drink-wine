from datetime import datetime

from app.models.client_model import Client
from app.models.order_model import Order
from app.models.product_model import Product
from app.models.provider_model import Provider
from flask import current_app, jsonify, request
from sqlalchemy.orm.exc import UnmappedInstanceError
from app.models.check_model import Check
from app.models.error_model import MissingKeyError, NotFound, WrongKeysError


def create_order():
    EXPECTED_KEYS = ["client_email", "provider_email", "products"]
    try:
        data = request.json

        Check.keys(EXPECTED_KEYS, data.keys())

        client_email = data.pop('client_email')
        provider_email = data.pop('provider_email')

        session = current_app.db.session

        client = Client.query.filter_by(email=client_email).first()

        if not client:
            raise NotFound("Client ")
        provider = Provider.query.filter_by(email=provider_email).first()

        if not provider:
            raise NotFound("Provider ")

        data['client_id'] = client.id
        data['provider_id'] = provider.id

        data['order_date'] = datetime.now()

        products = data.pop('products')

        order = Order(**data)

        for product in products:
            db_product = Product.query.filter_by(name=product.upper()).first()
        
            if not db_product:
                raise NotFound("Product ")

            order.products.append(db_product)

        session.add(order)
        session.commit()

        return jsonify(order), 201
    except NotFound as err:
        return err.message, 404
    except MissingKeyError as err:
        return err.message, 422
    except WrongKeysError as err:
        return err.message, 422


def delete_order(id: int):

    try:
        order = Order.query.get(id)

        session = current_app.db.session

        session.delete(order)
        session.commit()

        return '', 204
    except UnmappedInstanceError:
        return {'message': 'order not found!'}, 404

def get_order():
    orders = Order.query.all()

    return {"data": orders}, 200

def get_order_by_id(id:int):
    try:
        order = Order.query.get(id)

        if not order:
            raise NotFound("Order ")
        
        return {"data": order}
    except NotFound as err:
        return err.message, 404

