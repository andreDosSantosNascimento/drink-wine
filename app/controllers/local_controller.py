from app.models import city_model, country_model, state_model
from flask import current_app, jsonify, request


def create_country():
    data = request.json

    country_sigla = data['country_sigla'].upper()

    country_dict = {
        'sigla': country_sigla,
        'ddd': data['ddd']
    }

    try:
        country = country_model.Country(**country_dict)
        current_app.db.session.add(country)
        current_app.db.session.commit()
    except:
        return{'msg': 'Country already exists'}

    return jsonify(country), 201


def create_state():
    data = request.json

    try:
        country_sigla = data['country_sigla'].upper()
        country = country_model\
                .Country\
                .query\
                .filter(country_model.Country.sigla == country_sigla)\
                .first()        
        state_sigla = data['state_sigla'].upper()

        state_dict = {
            'sigla': state_sigla,
            'id_country': country.id
        }
    
    except:
        return {'msg': 'Invalid Country'}, 400

    try:
        state = state_model.State(**state_dict)
        current_app.db.session.add(state)
        current_app.db.session.commit()
    except:
        return{'msg': 'State already exists'}

    return jsonify(state), 201


def create_city():
    data = request.json

    try:
        state_sigla = data['state_sigla'].upper()
        state = state_model\
                .State\
                .query\
                .filter(state_model.State.sigla == state_sigla)\
                .first()

        id_state = state.id
    except:
        return {'msg': 'Invalid State'}, 400

    city_ddd = data['ddd']

    city_dict = {
        'ddd': city_ddd,
        'id_state': id_state
    }
    try:
        city = city_model.City(**city_dict)
        current_app.db.session.add(city)
        current_app.db.session.commit()
    except:
        return{'msg': 'City already exists'}

    return jsonify(city), 201
