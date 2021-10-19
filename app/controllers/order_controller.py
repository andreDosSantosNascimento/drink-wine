from datetime import datetime

from app.models.client_model import Client
from app.models.order_model import Order
from app.models.product_model import Product
from app.models.provider_model import Provider
from flask import current_app, jsonify, request
from sqlalchemy.orm.exc import UnmappedInstanceError


def create_order():

    data = request.json
    client_email = data.pop('client_email')
    provider_email = data.pop('provider_email')

    session = current_app.db.session

    client = Client.filter_by(email=client_email).one()
    provider = Provider.filter_by(email=provider_email).one()

    data['client_id'] = client.id
    data['provider_id'] = provider.id

    data['order_date'] = datetime.now()

    products = data.pop('products')

    order = Order(**data)

    for product in products:
        db_product = Product.query.filter_by(name=product['name']).first()
    
        if not db_product:
            db_product = Product(**product)
            session.add(db_product)
            session.commit()

        order.products.append(db_product)

    session.add(order)
    session.commit()

    return jsonify(order), 201


def delete_order(id: int):

    try:
        order = Order.query.get(id)

        session = current_app.db.session

        session.delete(order)
        session.commit()

        return '', 204
    except UnmappedInstanceError:
        return {'message': 'order not found!'}, 404


def update_order(id: int):

    data = request.json

    order = Order.query.get(id)

    if not order:
        return {'message': 'order not found!'}, 404

    Order.query.filter_by(id=id).update(data)

    current_app.db.session.commit()

    updated_order = Order.query.get(id)

    return jsonify(updated_order), 200
