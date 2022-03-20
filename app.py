from flask import Flask
from views.movies import movies_ns
from views.directors import directors_ns
from views.genres import genres_ns
from config import Config
from flask_restx import Api
from setup_db import db


def create_app():
    app = Flask(__name__)
    config = Config()
    app.config.from_object(config)
    create_extensions(app)
    return app


def create_extensions(app):
    api = Api(app)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)

    db.init_app(app)


app = create_app()

if __name__ == '__main__':
    app.run()
