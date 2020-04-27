from foxus import app, socketio
# from logs.logs import log_constructor
# log_constructor()

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=3008)
