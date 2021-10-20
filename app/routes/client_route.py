from app.controllers.client_controller import create_client, get_client, update_client, delete_client
from flask import Blueprint

bp = Blueprint('bp_client', __name__, url_prefix='/client')

bp.post('')(create_client)
bp.patch('/<int:id>')(update_client)
bp.delete('/<int:id>')(delete_client)
bp.get('')(get_client)