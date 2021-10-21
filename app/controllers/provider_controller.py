from app.models.error_model import (
    AlreadyRegisteredError,
    CityNotRegisteredError,
    InvalidError,
    NotFound,
    WrongNumberFormatError,
    WrongTypeError
    )

from app.models.provider_model import Provider
from app.models.country_model import Country
from flask import current_app, jsonify, request
import sqlalchemy
import psycopg2


def create_provider():
    try:
        data = request.json

        session = current_app.db.session

        sigla_country = data.pop('sigla_country')
        sigla_country = sigla_country.upper()

        country = Country.query.filter_by(sigla=sigla_country).first()

        data['country_id'] = country.id

        provider = Provider(**data)

        session.add(provider)
        session.commit()

        return jsonify(provider), 201
    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == psycopg2.errors.UniqueViolation:
            return AlreadyRegisteredError("Provider").message , 400
            
    except WrongTypeError as err:
        return err.message, 422

    except CityNotRegisteredError as err:
        return err.message, 422

    except InvalidError as err:
        return err.message, 400
    
    except WrongNumberFormatError as err:
        return err.message, 422

    except InvalidError as err:
        return err.message, 400

    except TypeError:
        return {"data": "Invalid keys detected"}, 422

def delete_provider(id: int):

    try:
        provider = Provider.query.get(id)

        if not provider:
            raise NotFound

        session = current_app.db.session

        session.delete(provider)
        session.commit()

        return '', 204

    except NotFound as err:
        return err.message, 404


def update_provider(id: int):
    try:
        data = request.json

        provider = Provider.query.get(id)

        if not provider:
            raise NotFound

        Provider.query.filter_by(id=id).update(data)

        current_app.db.session.commit()

        updated_provider = Provider.query.get(id)

    except NotFound as err:
        return err.message, 404

    except sqlalchemy.exc.InvalidRequestError:
        return {"data": "Invalid keys detected"}, 422

    return jsonify(updated_provider), 200

def get_provider():
    providers = Provider.query.all()
    return {"data": providers}, 200

def get_provider_by_id(id):
    try:
        provider = Provider.query.get(id)

        if not provider:
            raise NotFound
        
        return {"data": provider}
    except NotFound as err:
        return err.message, 404


