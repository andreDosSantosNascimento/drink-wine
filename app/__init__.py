from flask import Flask

from app.configs import database, env, migration
from app.routes import api_blueprint


def create_app():
    app = Flask(__name__)

    env.init_app(app)
    database.init_app(app)
    migration.init_app(app)
    app.register_blueprint(api_blueprint.bp)

    return app
