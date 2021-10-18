from app.controllers.client_controller import create_client, update_client, delete_client
from flask import Blueprint

bp = Blueprint('bp_client', __name__, url_prefix='/client')

bp.post(create_client)
bp.patch(update_client)
bp.delete(delete_client)