# coding=utf-8

from myapp import app
from model import FreshmanModel
from api import jsonify_with_data

@app.route('/freshman/list', methods=['GET'])
def get_freshman_list():
    fresh_model = FreshmanModel()
    res = fresh_model.get_freshman_list()
    return jsonify_with_data( res )
