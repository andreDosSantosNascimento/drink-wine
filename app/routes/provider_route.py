from app.controllers.provider_controller import create
from flask import Blueprint

bp = Blueprint('bp_provider', __name__, url_prefix='/provider')

bp.post('')(create)
