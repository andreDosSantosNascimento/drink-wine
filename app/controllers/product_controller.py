import psycopg2
import sqlalchemy
from app.models.check_model import Check
from app.models.errors_product import InvalidOrderDateError, InvalidValueuError
from app.models.product_model import Product
from flask import current_app, jsonify, request
from app.models.error_model import AlreadyRegisteredError, MissingKeyError, WrongKeysError


def create_product() -> dict:
    EXPECTED_KEYS = ["name", "value", "description", "expiration_date"]
    data = request.get_json()
    try:
        Check.keys(EXPECTED_KEYS, data.keys())

        product = Product(**data)
        session = current_app.db.session
        session.add(product)
        session.commit()

        return jsonify(product), 201

    except InvalidValueuError as e:
        return jsonify(e.message), 400

    except InvalidOrderDateError as e:
        return jsonify(e.message), 400
    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == psycopg2.errors.UniqueViolation:
            return AlreadyRegisteredError("Product").message , 400
    except MissingKeyError as err:
        return err.message, 422
    except WrongKeysError as err:
        return err.message, 422  
    


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
