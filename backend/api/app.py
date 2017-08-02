# coding=utf-8

from myapp import app
from model import AppModel
from api import jsonify_with_data
from flask import request

@app.route('/app/list', methods=['GET'])
def get_app_list():
    app_model = AppModel()
    res = app_model.get_app_list()
    if res:
        return jsonify_with_data( res )
    else:
        return jsonify_with_data( 'hehe' )
