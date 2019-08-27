from flask import Blueprint, request
import ccxt
import time
from api import make_response_ok, create_exchange

_kline = Blueprint("kline", __name__, url_prefix='/api/v1')


@_kline.route("kline/<path:symbol>", methods=['Get'], endpoint='kline')
def kline(symbol):
    exchange_name = request.args.get('ex')
   # symbol = request.args.get('symbol')
    timeframes = request.args.get('tf')  # timeframes
   # params = {'partial': False}
    exchange = create_exchange(exchange_name)
    #since = int(start.timestamp()*1000)
    time.sleep(exchange.rateLimit/1000)
    if exchange.has['fetchOHLCV']:
        return make_response_ok(exchange.fetch_ohlcv(symbol, timeframes))


@_kline.route("ticker/<path:symbol>", methods=['GET'], endpoint='ticker')
def ticker(symbol):
    exchange_name = request.args.get('ex')
    exchange = create_exchange(exchange_name)
    ticker = exchange.fetch_ticker(symbol)
    return make_response_ok(ticker)
