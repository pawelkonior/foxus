import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_socketio import SocketIO


db = SQLAlchemy()
socketio = SocketIO()

from foxus.database import UserModel, DataModel

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app(test_config=None):
    foxus = Flask(__name__, instance_relative_config=True)
    socketio.init_app(foxus)
    foxus.config.from_mapping(
        SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
        SQLALCHEMY_DATABASE_URI=f'sqlite:///{os.path.join(basedir, "backend.db")}'
    )

    if test_config is None:
        foxus.config.from_pyfile('config.py', silent=True)
    else:
        foxus.config.from_mapping(test_config)
    try:
        os.makedirs(foxus.instance_path)
    except OSError:
        pass

    db.init_app(foxus)
    # with foxus.app_context():
    #     db.create_all()
    #     db.session.commit()
    from . import views
    foxus.register_blueprint(views.bp)
    return foxus


app = create_app()
# app.app_context().push()

