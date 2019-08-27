import ccxt
from flask import Flask, Blueprint
from api import kline
app = Flask(__name__)

app.register_blueprint(kline.bp)
app.register_blueprint(order._order)


@app.route('/exchanges', methods=['GET'])
def get_exchanges():
    okcoin = ccxt.okcoinusd()
    markets = okcoin.load_markets()

    return markets


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
