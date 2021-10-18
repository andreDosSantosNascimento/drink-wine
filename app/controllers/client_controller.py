from app.models.client_model import Client
from flask import current_app, jsonify, request
from flask_jwt import JWT, jwt_required, current_identity

def create_client():
    data = request.json
    if not data['cpf'].isnumeric() or len(data['cpf'] != 11):
        return '', 400

    user = Client(**data)

    session = current_app.db.session
    session.add(user)
    session.commit()

    return user, 201
    ...

def update_client():
    data = request.json
    user = Client(**data)
    session = current_app.db.session
    session.patch(user)
    session.commit()
    return user, 200
    ...

def delete_client():
    data = request.json
    user = Client(**data)
    session = current_app.db.session
    session.delete(user)
    session.commit()

    return user, 200
    