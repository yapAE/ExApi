from flask import Blueprint, request
import ccxt
from api import make_response_ok, create_exchange

_order = Blueprint("order", __name__, url_prefix='/api/v1')


@_order.route("order_book/<path:symbol>", methods=['GET'], endpoint="order")
def order(symbol):
    exchange_name = request.args.get('ex_id')
    exchange = create_exchange(exchange_name)
    order_book = exchange.fetch_order_book(symbol)
    return make_response_ok(order_book)
