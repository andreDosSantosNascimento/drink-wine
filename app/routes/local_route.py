from app.controllers.local_controller import create_country, create_state, create_city
from flask import Blueprint

bp = Blueprint('bp_local', __name__, url_prefix='/local')

bp.post('/country')(create_country)
bp.post('/state')(create_state)
bp.post('/city')(create_city)
