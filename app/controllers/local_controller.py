from flask import Flask, jsonify, request, current_app
from app.models import city_model, country_model, state_model

def create_local():
    data = request.json

    country_sigla = data['country_sigla'].upper()

    country_dict = {
        'sigla': country_sigla,
        'ddd': data['country_ddd']
    }

    country = country_model.Country(**country_dict)
    current_app.db.session.add(country)
    current_app.db.session.commit()

    id_country = country.id
    state_sigla = data['state_sigla'].upper()

    state_dict = {
        'sigla': state_sigla,
        'id_country': id_country
    }

    state = state_model.State(**state_dict)
    current_app.db.session.add(state)
    current_app.db.session.commit()

    id_state = state.id
    city_ddd = data['city_ddd']

    city_dict = {
        'ddd': city_ddd,
        'id_state': id_state
    }

    city = city_model.City(**city_dict)
    current_app.db.session.add(city)
    current_app.db.session.commit()