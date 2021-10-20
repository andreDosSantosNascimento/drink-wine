import psycopg2
import sqlalchemy
from app.models.product_model import Product
from flask import current_app, jsonify, request


def create_product() -> dict:
    data = request.get_json()
    try:
        data['name'] = data['name'].upper()

        product = Product(**data)
        session = current_app.db.session
        session.add(product)
        session.commit()

        return jsonify(product), 201

    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == psycopg2.errors.UniqueViolation:
            return {'msg': 'Product already registered!'}, 400


def update_product(id: int) -> dict:
    data = request.get_json()
    Product.query.get(id)
    Product.query.filter_by(id=id).update(data)
    current_app.db.session.commit()
    product = Product.query.get(id)

    if product is None:
        return {'msg': 'Product Not Found'}, 404

    return jsonify(product), 200


def delete_product(id: int) -> dict:
    try:
        product = Product.query.get(id)
        current_app.db.session.delete(product)
        current_app.db.session.commit()
        return jsonify(product), 200
    except sqlalchemy.orm.exc.UnmappedInstanceError:
        return {'msg': 'Product Not Found'}, 404


def get_products():
    products = Product.query.all()
    return {"data": [{
        "id": product.id,
        "name": product.name,
        "value": product.value,
        "description": product.description,
        "expiration_date": product.expiration_date.strftime('%d/%m/%Y')
    } for product in products]}
