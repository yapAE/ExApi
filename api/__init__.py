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
