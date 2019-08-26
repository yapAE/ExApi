from flask import jsonify


def validsign(func):
    “”“
    验证签名
    ”“”

    def decorator():
        params = _get_request_params()
        appkey = params.get('appkey')
        sign = params.get('sign')
        csign = signature(params)
        if not appkey:
            return make_response_error(300, 'appkey is none.')
        if csign != sign:
            return make_response_error(500, 'signature is error.')

        return func()


return decorator


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
