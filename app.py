import ccxt
from flask import Flask, Blueprint
from api import exchange, kline, order, make_response_error
app = Flask(__name__)

app.register_blueprint(kline._kline)
app.register_blueprint(order._order)
app.register_blueprint(exchange._exchange)


@app.route('/')
def hello():
    data = {"msg": "Hello!"}
    return data


@app.errorhandler(404)
def not_found_error(error):
    return make_response_error(404, error.description)


@app.errorhandler(500)
def internal_error(error):
    return make_response_error(500, error.description)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
