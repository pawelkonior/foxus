from flask_socketio import emit
from flask import (
    Blueprint, render_template
)
from threading import Thread, Event

from foxus import socketio
from foxus.face_analysis import render_face, calculate_data


bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
def index():
    return render_template('index.html')


thread = Thread()
thread_stop_event = Event()


@socketio.on('connect')
def chart_data_connect():
    global thread
    print('Client connected')
    emit('connected')
    if not thread.is_alive():
        print("Starting Thread")
        thread = socketio.start_background_task(data_generator)


def data_generator():
    while not thread_stop_event.isSet():
        data = calculate_data(1)
        socketio.emit('connected')
        socketio.emit('user processed', data)
        socketio.sleep(1)


@socketio.on('stream')
def handle_stream(message):
    new_frame = render_face(message['id'], message['stream'])

    emit('stream processed', message['stream'])
