from flask import Blueprint
from app.controllers.order_controller import create_order, delete_order, update_order

bp = Blueprint('bp_order', __name__, url_prefix='/orders')

bp.post('')(create_order)
bp.patch('<int:id>')(update_order)
bp.delete('<int:id>')(delete_order)
