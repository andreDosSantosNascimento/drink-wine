from app.models.city_model import City
from app.models.client_model import Client
import psycopg2
import sqlalchemy
from flask import current_app, jsonify, request

from app.models.error_model import (
    AlreadyRegisteredError,
    CityNotRegisteredError,
    InvalidCnpjError,
    InvalidEmailError,
    WrongNumberFormatError,
    WrongTypeError,
    NotFound
    )

def create_client() -> dict:
    try:
        data = request.get_json()
        ddd = data.pop("ddd_city")
        
        city_id =  City.query.filter_by(ddd = ddd).first()
        
        if not city_id : 
            raise CityNotRegisteredError
        
        data["city_id"] = city_id.id

        client = Client(**data)
        session = current_app.db.session
        session.add(client)
        session.commit()

        return jsonify(client), 201

    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == psycopg2.errors.UniqueViolation:
            return AlreadyRegisteredError("Client").message , 400
            
    except WrongTypeError as err:
        return err.message, 422

    except CityNotRegisteredError as err:
        return err.message, 422

    except InvalidCnpjError as err:
        return err.message, 400
    
    except WrongNumberFormatError as err:
        return err.message, 422

    except InvalidEmailError as err:
        return err.message, 400

def update_client(id: int) -> dict:
    try:
        data = request.get_json()

        if "ddd_city" in data:
            ddd = data.pop("ddd_city")

            city_id =  City.query.filter_by(ddd = ddd).first()

            if not city_id : 
                raise CityNotRegisteredError

            data["city_id"] = city_id.id

        Client.query.get(id)
        Client.query.filter_by(id=id).update(data)
        current_app.db.session.commit()
        client = Client.query.get(id)

        if not client:
            raise NotFound

        return "", 204

    except CityNotRegisteredError as err:
        return err.message, 422

    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == psycopg2.errors.UniqueViolation:
            return AlreadyRegisteredError("Some data are").message , 400

    except NotFound as err:
        return err.message, 404

def delete_client(id: int) -> dict:
    try:
        client = Client.query.get(id)

        if not client:
            raise NotFound

        current_app.db.session.delete(client)
        current_app.db.session.commit()

        return "", 204

    except NotFound as err:
        return err.message, 404

def get_client() -> dict:
    clients = Client.query.all()
    return {"data": [{
        "id": client.id,
        "name": client.name,
        "email": client.email,
        "phone": client.phone,
        "cnpj": client.cnpj,
        "city_id": client.city_id,
    } for client in clients]}



