import logging
from flask import Flask
from flask import request
import requests


log_level = logging.DEBUG
logging.basicConfig(format='%(asctime)s %(message)s', level=log_level)

app = Flask(__name__)

@app.route('/login')
def login_handler():
    logging.debug("Processing login")
    r = requests.get("http://m:8080/login_data")
    return r.json()


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
