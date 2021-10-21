from app.controllers.client_controller import (create_client, delete_client,
                                               get_client, get_client_by_id, update_client)
from flask import Blueprint

bp = Blueprint('bp_client', __name__, url_prefix='/client')

bp.post('')(create_client)
bp.patch('/<int:id>')(update_client)
bp.delete('/<int:id>')(delete_client)
bp.get('')(get_client)
bp.get('/<int:id>')(get_client_by_id)

