# coding=utf-8
from time import time
import json
from flask import jsonify


class APIStatus:
    OK = (200, 'OK')
    BAD_REQUEST = (400, 'Bad_request')
    UNAUTHORIZED = (401, 'Unauthorized')
    NOT_FOUND = (404, 'Not_found')
    FORBIDDEN = (403, 'Forbidden')


class RETStatus:
    OK = (0, '')
    TIME_OUT = (1, '请求超时，请稍后重试')
    REQUEST_TIME_OUT = (1001, '网络请求超时')


def jsonify_with_data( data, ret=None, status=None, timestamp=int(time()) ):
    if ret is None:
        ret = RETStatus.OK
    if status is None:
        status = APIStatus.OK
    resp = {'content': data, 'msg': ret[1], 'ret': ret[0], 'timestamp': timestamp}
    resp = jsonify(resp)
    resp.status_code = status[0]
    return resp

from index import *
from freshman import *
from product import *
from task import *
from app import *
