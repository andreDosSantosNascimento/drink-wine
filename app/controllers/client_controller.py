from app.models.client_model import Client
import psycopg2
import sqlalchemy
from flask import current_app, jsonify, request

def create_client() -> dict:
    try:
        data = request.get_json()

        client = Client(**data)
        session = current_app.db.session
        session.add(client)
        session.commit()

        return jsonify(client), 201

    except sqlalchemy.exc.IntegrityError as e:
        if type(e.orig) == psycopg2.errors.UniqueViolation:
            return {'msg': 'Client already registered!'}, 400

def update_client(id: int) -> dict:
    data = request.get_json()
    Client.query.get(id)
    Client.query.filter_by(id=id).update(data)
    current_app.db.session.commit()
    client = Client.query.get(id)

    if client is None:
        return {'msg': 'Client Not Found'}, 404

    return jsonify(client), 200

def delete_client(id: int) -> dict:
    try:
        client = Client.query.get(id)
        current_app.db.session.delete(client)
        current_app.db.session.commit()
        return jsonify(client), 200
    except sqlalchemy.orm.exc.UnmappedInstanceError:
        return {'msg': 'Client Not Found'}, 404

def get_client():
    clients = Client.query.all()
    return {"data": [{
        "id": client.id,
        "name": client.name,
        "email": client.email,
        "phone": client.phone,
        "cnpj": client.cnpj,
        "city_id": client.city_id,
    } for client in clients]}


