from app.controllers.local_controller import (create_city, create_country,
                                              create_state, get_local)
from flask import Blueprint

bp = Blueprint('bp_local', __name__, url_prefix='/local')

bp.post('/country')(create_country)
bp.post('/state')(create_state)
bp.post('/city')(create_city)
bp.get('')(get_local)
