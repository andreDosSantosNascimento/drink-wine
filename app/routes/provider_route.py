from app.controllers.provider_controller import create_provider, delete_provider, update_provider
from flask import Blueprint

bp = Blueprint('bp_provider', __name__, url_prefix='/provider')

bp.post('')(create_provider)
bp.patch('<int:id>')(update_provider)
bp.delete('<int:id>')(delete_provider)
