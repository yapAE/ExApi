from flask import Blueprint
from api import make_response_ok, create_exchange
import ccxt

_exchange = Blueprint("exchange", __name__, url_prefix='/api/v1')


@_exchange.route("exchanges", methods=['GET'], endpoint='exchanges')
def exchanges():
    # 列出所有交易所
    return make_response_ok(ccxt.exchanges)


@_exchange.route("exchanges/<exchange>/<attr>", methods=['GET'], endpoint='item')
def item(exchange, attr):
    exchange = create_exchange(exchange)
    exchange.load_markets()
    data = getattr(exchange, attr)
    return make_response_ok(data)
