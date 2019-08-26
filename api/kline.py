from flask import Blueprint
import ccxt
import time

bp = Blueprint("data", __name__, url_prefix='api/v1/data')


def create_exchange(exchange_name):
    # 创建交易所
    exchange = getattr(ccxt, exchange_name)()
    exchange.load_markets()
    return exchange


@bp.route("data", methods=['Get'], endpoint='kline')
def kline(exchange_name, symbol, timeframes):
   # params = {'partial': False}
    exchange = create_exchange(exchange_name)
    #since = int(start.timestamp()*1000)
    time.sleep(exchange.rateLimit/1000)
    if exchange.has['fetchOHLCV']:
        return exchange.fetch_ohlcv(symbol, timeframes)
