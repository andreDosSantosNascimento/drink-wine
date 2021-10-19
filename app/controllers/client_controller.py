from app.models.client_model import Client
from flask import current_app, jsonify, request




def create_client():
    data = request.get_json()

    if not data['cnpj'].isnumeric() or len(data['cnpj']) != 14:
        return '', 400

    user = Client(**data)

    session = current_app.db.session
    session.add(user)
    session.commit()

    return jsonify(user), 201
    ...

def update_client():
    data = request.get_json()

    user = Client(**data)
    session = current_app.db.session
    session.patch(user)
    session.commit()
    return jsonify(user), 200
    ...

def delete_client():
    data = request.get_json()

    user = Client(**data)
    session = current_app.db.session
    session.delete(user)
    session.commit()

    return jsonify(user), 200
    ...

def get_client(id):
    client = Client.query.get(id)

    if not client:
        return {"msg": "Not found!"}, 404
        
    return jsonify(client), 200
    ...