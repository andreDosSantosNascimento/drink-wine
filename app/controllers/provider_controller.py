from app.models.provider_model import Provider
from app.models.country_model import Country
from flask import current_app, jsonify, request
from sqlalchemy.orm.exc import UnmappedInstanceError


def create_provider():

    data = request.json

    session = current_app.db.session

    sigla_country = data.pop('sigla_country')

    sigla_country = sigla_country.upper()

    if not data['phone'].isnumeric():
        return {'message': 'Phone only contains numbers.'}, 400

    if not data['nif'].isnumeric():
        return {'message': 'NIF only contains numbers.'}, 400

    country = Country.query.filter_by(sigla=sigla_country).first()

    if not country:
        return {'message': 'This country not exists.'}, 400

    data['country_id'] = country.id

    provider = Provider(**data)

    session.add(provider)
    session.commit()

    return jsonify(provider), 201


def delete_provider(id: int):

    try:
        provider = Provider.query.get(id)

        session = current_app.db.session

        session.delete(provider)
        session.commit()

        return '', 204
    except UnmappedInstanceError:
        return {'message': 'provider not found!'}, 404


def update_provider(id: int):

    data = request.json

    provider = Provider.query.get(id)

    if not provider:
        return {'message': 'provider not found!'}, 404

    Provider.query.filter_by(id=id).update(data)

    current_app.db.session.commit()

    updated_provider = Provider.query.get(id)

    return jsonify(updated_provider), 200
