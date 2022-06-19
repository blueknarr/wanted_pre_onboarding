from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    from . import models
    db.init_app(app)
    migrate.init_app(app, db)

    # Blueprint
    from app.views import main, api
    app.register_blueprint(main.bp)
    app.register_blueprint(api.bp)

    return app