from app.routes.client_route import bp as client_bp
from app.routes.local_route import bp as local_bp
from app.routes.order_route import bp as order_bp
from app.routes.product_route import bp as product_bp
from app.routes.provider_route import bp as provider_bp
from flask import Flask


def init_app(app: Flask):
    app.register_blueprint(provider_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(local_bp)
    app.register_blueprint(client_bp)
