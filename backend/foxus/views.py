from flask import (
    Blueprint, render_template
)

from threading import Thread, Event
from foxus.sockets_foxus import run_socket_connections

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('/')
def index():
    run_thread_for_sockets()
    return render_template('index.html')


thread = Thread()
thread_stop_event = Event()


def run_thread_for_sockets():
    global thread
    if not thread.is_alive():
        print("Starting Thread")
        run_socket_connections()


