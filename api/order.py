from flask import Blueprint, request
import ccxt
from api import make_response_ok, create_exchange

_order = Blueprint("order", __name__, url_prefix='/api/v1')


@_order.route("order-book/<path:symbol>", methods=['GET'], endpoint="order")
def order(symbol):
    exchange = create_exchange('ex')
    order_book = exchange.fetch_order_book(symbol)
    return make_response_ok(order_book)


@_order.route("trades/<path:symbol>", methods=['GET'], endpoint='trades')
def trades(symbol):
  #  limit = request.args.get('limit')
    exchang = create_exchange('ex')
    trades = exchang.fetch_trades(symbol)
    return make_response_ok(trades)
