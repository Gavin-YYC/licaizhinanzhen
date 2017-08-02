# coding=utf-8

from myapp import app
from model import ProductModel
from api import jsonify_with_data
from flask import request

@app.route('/product/list', methods=['GET'])
def get_product_list():
    
    p_type = int(request.args.get('type'))
    p_status = int(request.args.get('status'))
    p_threshold = eval(request.args.get('threshould'))
    p_yield_rate = eval(request.args.get('profitRate'))
    p_cycle = eval(request.args.get('cycle'))
    p_risk_level = eval(request.args.get('riskLevel'))
    p_process = eval(request.args.get('process'))
    p_bank_deposit = int(request.args.get('bankDeposit'))
    

        
    # 实例化model
    product_model = ProductModel()
    
    
    # 根据类型分发
    # 活期 type = 1 
    if p_type == 1:
    	res = product_model.get_current_account_list( p_type, p_status, p_threshold, p_yield_rate, p_risk_level, p_process, p_bank_deposit )
    # 定期 type = 2
    elif p_type == 2:
    	res = product_model.get_fixed_deposit_list( p_type, p_status, p_threshold, p_yield_rate, p_cycle, p_risk_level, p_process, p_bank_deposit )
    elif p_type == 3:
        res = ''
    elif p_type == 4:
        res = ''
    else:
        res = ''
        
    return jsonify_with_data( res )
