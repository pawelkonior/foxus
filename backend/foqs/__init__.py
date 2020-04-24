import os

from flask import Flask


def create_app(test_config=None):
    foqs = Flask(__name__, instance_relative_config=True)
    foqs.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        foqs.config.from_pyfile('config.py', silent=True)
    else:
        foqs.config.from_mapping(test_config)

    try:
        os.makedirs(foqs.instance_path)
    except OSError:
        pass

    from . import views
    foqs.register_blueprint(views.bp)

    return foqs


app = create_app()
