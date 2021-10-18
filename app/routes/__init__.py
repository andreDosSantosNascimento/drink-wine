from app.routes.product_route import bp as product_bp
from app.routes.provider_route import bp as provider_bp
from flask import Flask


def init_app(app: Flask):
    app.register_blueprint(provider_bp)
    app.register_blueprint(product_bp)
