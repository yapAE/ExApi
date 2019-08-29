import ccxt
from flask import jsonify, request


def _get_request_param(key):
    value = request.form.get(key)
    if not value:
        value = request.args.get(key)
    return value


def _get_request_params():
    params = request.form
    if not params:
        params = request.args
    return params


def make_response_ok(data=None):
    resp = {'code': 0, 'msg': 'success'}
    if data:
        resp['data'] = data
    return jsonify(resp)


def make_response_error(code, msg):
    resp = {'code': code, 'msg': msg}
    return jsonify(resp)

# Exchange


def create_exchange(exchange_id):
    # 创建交易所
    exchange_name = _get_request_param(exchange_id)
    if not exchange_name:
        exchange_name = exchange_id
    exchange = getattr(ccxt, exchange_name)()
    return exchange
