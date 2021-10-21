from app.controllers.provider_controller import create_provider, delete_provider, get_provider, get_provider_by_id, update_provider
from flask import Blueprint

bp = Blueprint('bp_provider', __name__, url_prefix='/provider')

bp.post('')(create_provider)
bp.patch('<int:id>')(update_provider)
bp.delete('<int:id>')(delete_provider)
bp.get('')(get_provider)
bp.get('<int:id>')(get_provider_by_id)

