from flask import Blueprint, request
import ccxt
from api import make_response_ok, create_exchange

_order = Blueprint("order", __name__, url_prefix='/api/v1')


@_order.route("order-book/<path:symbol>", methods=['GET'], endpoint="order")
def order(symbol):
    exchange_name = request.args.get('ex')
    exchange = create_exchange(exchange_name)
    order_book = exchange.fetch_order_book(symbol)
    return make_response_ok(order_book)


@_order.route("trades/<path:symbol>", methods=['GET'], endpoint='trades')
def trades(symbol):
    exchange_name = request.args.get('ex')
    limit = request.args.get('limit')
    exchang = create_exchange(exchange_name)
    trades = exchang.fetch_trades(symbol, limit)
    return make_response_ok(trades)
