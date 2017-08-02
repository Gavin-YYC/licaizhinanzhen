# coding=utf-8

from myapp import app
from flask import render_template, request, json
from api import jsonify_with_data
from worker import Spider
from service import ProductService
from pyquery import PyQuery as pq
import re
import time
import urlparse
import requests

@app.route('/task', methods=['GET'])
def task():

    app = request.args.get('app')
    p_type = int(request.args.get('type'))

    if app is not None and p_type is not None:
        if app == 'baidu':
            res = baidu( p_type )
        elif app == 'jingdong':
            res = jingdong( p_type )
        elif app == 'fenghuang':
            res = fenghuang( p_type )
        elif app == 'qq':
            res = qq( p_type )
        elif app == 'yangqianguan':
            res = yangqianguan( p_type )
        elif app == 'suishouji':
            res = suishouji( p_type )
        elif app == 'wukong':
            res = wukong( p_type )
        elif app == 'zhaoshang':
            res = zhaoshang( p_type )
        elif app == 'zhaozhaolicai':
            res = zhaozhaolicai( p_type )
    else:
        res = False

    # if res:
    #     msg = 'ok'
    # else:
    #     msg = 'false'

    return jsonify_with_data( res )


# 百度
def baidu( p_type ):
    spider = Spider()
    product_service = ProductService()
    fixed_url = 'https://8.baidu.com/h5/regular/finance/sale_project/v2?page_no=1&page_size=100&sell_type=1&channel=4'
    data = json.loads( spider.get_data( fixed_url ) )
    res_data = []
    for row in data["project_info_list"]:
        itemIds = row["project_code"]
        url = "https://8.baidu.com/h5/exchange/get_item_info?from=0.0.0&trans_place=5&item_id=" + str(itemIds) + "&channel=4"
        res = json.loads( spider.get_data( url ) )
        if res["ret"] == "0":
            res_info = res["ret_info"]
            res_info["source_url"] = url
            res_data.append( res_info )
    res = product_service.baidu_set_data( res_data )
    return res

# 京东
def jingdong( p_type ):
    spider = Spider()
    product_service = ProductService()

    def get_url( pageNo ):
        return 'https://dq.jd.com/getDalicai?callback=jQuery1830932213288738319_1492881294892&order=&pageSize=12&pageNo=' + str(pageNo) + '&label=0&termNo=&amountNo=&channel=pc&type=bxlc%7Cgslc%7Cbylc%7Cbill%7Cqslc&_=1492881294989'

    def getData_JD( url ):
        data = spider.get_data( url )
        l_index = data.find('{')
        r_index = data.rfind('}')
        data = json.loads(data[l_index:r_index+1])
        return data

    def get_ding_data():
        pageNo = 1
        fixed_url = get_url( pageNo )
        data = getData_JD( fixed_url )
        datas = data["datas"]
        pages = data["paginator"]
        for i in range(1, pages["pages"]):
            fixed_url = get_url( pageNo + 1 )
            new_data = getData_JD( fixed_url )
            datas = datas + new_data["datas"]
        res = product_service.jd_set_data( datas )
        return res

    def get_huo_data():
        lingyongqian_url = 'http://xjk.jr.jd.com/gold/charts?productCode=J50060000'
        licaijin_url = 'http://xjk.jr.jd.com/gold/charts?productCode=J50060001'

        lingyongqian_data = spider.get_data( lingyongqian_url )
        licaijin_data = spider.get_data( licaijin_url )

        print lingyongqian_data
        return 'aa'

    # 活期数据
    if p_type == 1:
        return get_huo_data()

    # 定期数据
    elif p_type == 2:
        return get_ding_data()

# 凤凰金融
def fenghuang( p_type ):
    spider = Spider()
    product_service = ProductService()

    huo_url = 'https://lc.fengjr.com/loan/fhy?type=FENG_FIXED_CURRENT'
    ding_url = 'https://lc.fengjr.com/api/v2/loan/list?version=3.4&dir=FENG_CX&uid=&page=1&pageSize=10&_=1492943620171'
    data = spider.get_data( ding_url )

    def get_ding_data( ding_url ):
        data = json.loads(spider.get_data( ding_url ))
        data = data["data"]["list"]
        res = product_service.fh_set_data( data )
        return res

    def get_huo_date( huo_url ):
        # name, yeild, threshold, desc, source_url, app_id, item_id, status=1, process=0, risk_level=1, bank_authority=0
        data = spider.get_data( huo_url )
        doc = pq( data )
        prifit = doc('.banner .number').eq(0).html()
        res = product_service.common_set_huo_data( u'零钱'.encode('utf-8'), prifit, '1000', u'灵活存取'.encode('utf-8'), huo_url, 3 )
        return res

    if p_type == 1:
        return get_huo_date( huo_url )
    elif p_type == 2:
        return get_ding_data( ding_url )

# 腾讯理财通
def qq( p_type ):
    spider = Spider()
    product_service = ProductService()
    home_url = 'https://qian.qq.com/app/v2.0/pc_fund_query_supportsp_with_last_profit.cgi'
    data = eval(spider.get_data( home_url ))
    arr = data["Array"]
    arr.extend(data["nonstand_list"])

    # duration_type 1 - 天，2-月
    def change_cycle( dur, a_type ):
        if a_type is None:
            return int(dur)
        a_type = int( a_type )
        if a_type == 1:
            return dur
        elif a_type == 2:
            return 30 * int(dur)

    def get_product_code( item ):
        if "product_code" in item:
            return item["product_code"]
        else:
            return ''

    def get_something( item, a, b=None ):
        if a in item:
            return item[a]
        if b is not None:
            if b in item:
                return item[b]
        return None

    def get_end(item, a):
        if a in item:
            return item[a]
        return ''

    for item in arr:
        # 活期
        a_type = int(item["fund_type"])
        if a_type == 1 or a_type == 3:
            res = product_service.common_set_huo_data(
                item["partner_nickname"],
                int(get_something(item, 'day7_profit_rate', 'expected_one_year_profit_rate'))/1000000.0,
                item["buy_lower_limit"],
                '随存随取',
                "https://qian.qq.com/web/v2/detail/" + item["fund_code"] + ".shtml?stat_data=fm_1_index_1&product_code=" + get_product_code(item),
                4, item["fund_code"] + "," + get_product_code(item), 1, 0, item["sp_risk_type"], 0)
        # 定期
        elif a_type == 2 or a_type == 5:
            product_service.common_set_ding_data(
                item["partner_nickname"],
                change_cycle(get_something(item, 'duration', 'investment_term'), get_something(item, "duration_type")),
                int(get_something(item, 'day7_profit_rate', 'expected_one_year_profit_rate'))/1000000.0,
                item["buy_lower_limit"], get_something(item, 'product_name', 'fund_name'),
                "https://qian.qq.com/web/v2/detail/" + item["fund_code"] + ".shtml?stat_data=fm_1_index_1&product_code=" + get_product_code(item),
                4, 1, '', get_end(item, "buy_end_time"), item["fund_code"] + "," + get_product_code(item), '',
                0, item["sp_risk_type"], 0)
    return 'ok'


# 洋钱罐
def yangqianguan( p_type ):
    spider = Spider()
    product_service = ProductService()
    home_url = 'https://www.yangqianguan.com/api/homepage/getMobileHomepage'
    data = json.loads(spider.get_data( home_url ))
    print data
    data = data["body"]["featureProductCardVOList"]
    fixed_pro = [15, 14, 16, 38]

    def get_cycle( text ):
        res = re.match(r'\d+',text)
        return int(res.group().strip())

    for item in data:
        # 活期
        card_id = int(item["featureProductCardId"])
        if card_id == 12:
            product_service.common_set_huo_data(
                item["name"], item["rate"], 1, item["lockInPeriodDescription"], 'https://www.yangqianguan.com/', 5,
                item["featureProductCardId"])
        # 定期
        elif card_id in fixed_pro:
            product_service.common_set_ding_data(
                item["name"], get_cycle(item["lockInPeriodDescription"]), item["rate"], '100', item["description"],
                'https://www.yangqianguan.com/', 5, 1, 0, '', item["featureProductCardId"])
    return 'ok'


# 随手记
def suishouji( p_type ):
    spider = Spider()
    product_service = ProductService()
    home_url = 'https://lc.feidee.com/p2p/steady/list'
    data = json.loads(spider.get_data( home_url ))
    data = data["zxProductList"]

    def change_status( status ):
        status = int( status )
        if status == 2:
            return 1
        elif status == 1 or status == 3:
            return 3
        else:
            return 1

    for item in data:
        url = urlparse.urlparse(item["url"])
        params = urlparse.parse_qs(url.query,True)
        item_id = params["productNo"][0]
        product_service.common_set_ding_data(
            item["productName"], item["borrowTime"], item["annualRate"], item["minAmount"],
            item["interestContent"], item["url"], 6, change_status(item["saleStatus"]),
            0, '', item_id, time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(item["calculInterestDate"]["time"])/1000)),
            str(item["progress"]), 1, 0)
    return 'ok'


# 悟空理财
def wukong( p_type ):
    spider = Spider()
    product_service = ProductService()
    home_url = 'https://m.wukonglicai.com/weixin/recommendPageInfo.html'
    data = json.loads(spider.get_data( home_url ))
    data = data["productInfoVo"]

    def change_times( num, type ):
        if type == 'M':
            return str(int(num) * 30)
        else:
            return num

    for item in data:
        # 活期
        if item["productType"] == 'H':
            # name, yeild, threshold, desc,
            # source_url, app_id, item_id, status=1, process=0,
            # risk_level=1, bank_authority=0
            product_service.common_set_huo_data(
                item["productName"], item["baseYields"], item["minInvest"], item["timeLong"],
                "https://m.wukonglicai.com/weixin/current/investDetail.html", 7, 'current_wklc')
        # 定期
        else:
            # name, cycle, yeild, threshold,
            # desc, source_url, app_id, status=1,
            # purchaseLimit=0, purchase_stop_time='', item_id='', received_time='',
            # process=0, risk_level=1, bank_authority=0
            product_service.common_set_ding_data(
                item["productName"], change_times(item["timeLong"], item["productType"]), item["baseYields"], item["minInvest"],
                item["mdesc"] or '', "https://m.wukonglicai.com/weixin/investDetail.html?pCode=" + item["productCode"], 7, 1,
                item["maxInvest"], '', item["productCode"], '', 0, 1, 0)
    return 'ok'

# 招商银行
def zhaoshang( p_type ):
    spider = Spider()
    product_service = ProductService()
    base_url = 'https://ai.cmbchina.com/mbweb/subpage/SubPageService.ashx?service=list&subpage=product&catalogIndex='
    huo_url = base_url + '0'
    ding_url = base_url + '2'

    def get_huo_data( url ):
        data = eval(spider.get_data( url ))
        for item in data:
            # name, yeild, threshold, desc,
            # source_url, app_id, item_id, status=1, process=0,
            # risk_level=1, bank_authority=0
            product_service.common_set_huo_data(
                item["Name"], item["ExpectedRate"], item["Amount"], item["timeLong"],
                "http://www.cmbchina.com/cfweb/personal/productdetail.aspx?code=" + item["ProductCode"], 8, item['ProductCode'])

    def get_ding_data( url ):
        data = eval(spider.get_data( url ))
        pass

    if p_type == 1:
        get_huo_data( huo_url )
    elif p_type == 2:
        get_ding_data( ding_url )


# 招招理财
def zhaozhaolicai( p_type ):
    spider = Spider()
    product_service = ProductService()
    base_url = 'https://zhaozhaolicai.com/api'
    payload = "KInGDOM=MTQ5MzIyOTY5ODM4OA%3D%3D&KINGdOM=a2luZ2RvbS5rZmF0LmdldF9mdW5kYmFzZV9pbmZv&KINGDoM=VjIuMA%3D%3D&KiNGDOM=JTdCJTIyY2F0X3ZhcmlldGllcyUyMiUzQSUyMjElMjIlMkMlMjJwYWdlTnVtYmVyJTIyJTNBJTIyMSUyMiUyQyUyMnBhZ2VTaXplJTIyJTNBJTIyMTAlMjIlN0Q%3D&kINGDOM=460DA09D0004D84841C8C3DF9BF52D0E&KINgDOM=emhhb3poYW9saWNhaS5jb20%3D&KINGDOm=aHR0cHM6"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache"
    }
    response = requests.request("POST", base_url, data=payload, headers=headers)
    data = json.loads(response.text)
    data = data["kdjson"]["items"]

    def get_process( item, statue ):
        all_status = ["3", "4", "6", "7"]
        if statue in all_status:
            return 100
        else:
            return float(item["amountprop"]) * 100

    def get_status( item, status ):
        if status == '2':
            return 1
        elif status == '3':
            return 3

    for item in data:
        # name, cycle, yeild, threshold,
        # desc, source_url, app_id, status=1,
        # purchaseLimit=0, purchase_stop_time='', item_id='', received_time='',
        # process=0, risk_level=1, bank_authority=0
        product_service.common_set_ding_data(
            item["fundname"], item["deadlinesort"], item["annualrate"], item["mintendtenderedsum"],
            item["paymentmodename"] or '', "https://zhaozhaolicai.com/product/productDetail.html?id=" + item["fundcode"], 8, get_status(item, item["fundstatus"]),
            0, item["endtranstime"], item["fundcode"], item["interestdate"], get_process(item, item["fundstatus"]), int(item["fundrisklevel"]), 0)

    payload = "css=MTQ5MzMxNDI1MTQ1Ng%3D%3D&android=a2luZ2RvbS5rZmF0LmdldF9mdW5kYmFzZV9pbmZv&html=VjIuMA%3D%3D&ios=JTdCJTIyY2F0X3ZhcmlldGllcyUyMiUzQSUyMjIlMjIlMkMlMjJwYWdlTnVtYmVyJTIyJTNBJTIyMSUyMiUyQyUyMnBhZ2VTaXplJTIyJTNBJTIyMTAlMjIlN0Q%3D&js=2C1D8F336C63C1CC4369973E17EB4E04&wp=emhhb3poYW9saWNhaS5jb20%3D"
    response = requests.request("POST", base_url, data=payload, headers=headers)
    data = json.loads(response.text)
    data = data["kdjson"]["items"]

    for item in data:
            # name, yeild, threshold, desc,
            # source_url, app_id, item_id, status=1, process=0,
            # risk_level=1, bank_authority=0
            product_service.common_set_huo_data(
                item["fundname"], item["annualrate"], item["mintendtenderedsum"], '灵活稳健 转出实时到账',
                "https://zhaozhaolicai.com/product/productDetail.html?id=" + item["fundcode"], 8, item['fundcode'], 1, 0,
                int(item["fundrisklevel"]), 0)

    return 'ok'
