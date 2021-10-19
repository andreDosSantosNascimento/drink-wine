from app.controllers.product_controller import (create_product, delete_product, get_products,
                                                update_product)
from flask import Blueprint

bp = Blueprint('bp_product', __name__, url_prefix='/product')

bp.post('')(create_product)
bp.delete('/<int:id>')(delete_product)
bp.patch('/<int:id>')(update_product)
bp.get('')(get_products)
