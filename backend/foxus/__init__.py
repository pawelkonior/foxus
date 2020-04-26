import os

from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from engineio.payload import Payload


Payload.max_decode_packets = 500

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

socketio = SocketIO(app)
app.config['SECRET_KEY'] = '~t\x8d\xb3\xb1t*\xe6\xf5\xd2\x7f\xb0P\xafI\x94\xbdX'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "backend.db")}'
# db = SQLAlchemy(app)

from foxus.views import bp
app.register_blueprint(bp)



