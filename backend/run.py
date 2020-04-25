from foqs import app
from logs.logs import log_constructor
log_constructor()

if __name__ == "__main__":
    app.run(debug=True, port=4000)
