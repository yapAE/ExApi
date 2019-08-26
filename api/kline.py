from flask import Blueprint, request
import ccxt
import time
from api import make_response_ok

bp = Blueprint("data", __name__, url_prefix='/api/v1/data')


def create_exchange(exchange_name):
    # 创建交易所
    exchange = getattr(ccxt, exchange_name)()
    exchange.load_markets()
    return exchange


@bp.route("/kline", methods=['Get'], endpoint='kline')
def kline():
    exchange_name = request.args.get('exchange_name')
    symbol = request.args.get('symbol')
    timeframes = request.args.get('timeframes')
   # params = {'partial': False}
    exchange = create_exchange(exchange_name)
    #since = int(start.timestamp()*1000)
    time.sleep(exchange.rateLimit/1000)
    if exchange.has['fetchOHLCV']:
        return make_response_ok(exchange.fetch_ohlcv(symbol, timeframes))


@bp.route("/test", methods=['GET'], endpoint='test')
def test():
    exchange_name = request.args.get('exchange_name')
    exchange = create_exchange(exchange_name)
    for symbol in exchange.markets:
        time.sleep(exchange.rateLimit/1000)
        print(symbol, exchange.fetch_ohlcv(symbol, '1d'))
