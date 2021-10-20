from app.routes import (client_route, local_route, order_route, product_route,
                        provider_route)
from flask import Blueprint

bp = Blueprint('api_bp', __name__, url_prefix='/api')


bp.register_blueprint(client_route.bp)
bp.register_blueprint(local_route.bp)
bp.register_blueprint(order_route.bp)
bp.register_blueprint(product_route.bp)
bp.register_blueprint(provider_route.bp)
