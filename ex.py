import ccxt
from flask import Flask, jsonify
app = Flask(__name__)


@app.route('/api/v1/exchanges', methods=['GET'])
def get_exchanges():
    okcoin = ccxt.okcoinusd()
    markets = okcoin.load_markets()

    return markets


if __name__ == '__main__':
    app.run(debug=True)
