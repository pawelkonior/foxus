import os

from flask import Flask


def create_app(test_config=None):
    foxus = Flask(__name__, instance_relative_config=True)
    foxus.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        foxus.config.from_pyfile('config.py', silent=True)
    else:
        foxus.config.from_mapping(test_config)

    try:
        os.makedirs(foxus.instance_path)
    except OSError:
        pass

    from . import views
    foxus.register_blueprint(views.bp)

    return foxus


app = create_app()
