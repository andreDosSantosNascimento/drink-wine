from flask import Blueprint
from app.controllers.order_controller import create_order, delete_order, get_order, get_order_by_id

bp = Blueprint('bp_order', __name__, url_prefix='/orders')

bp.post('')(create_order)
bp.delete('<int:id>')(delete_order)
bp.get('')(get_order)
bp.get('<int:id>')(get_order_by_id)

