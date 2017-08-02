# coding=utf-8

from model import ProductModel

class ProductService( object ):

    risk_level = {
        u"低": 1,
        u"中低": 2,
        u"中": 3,
        u"中高": 4,
        u"高": 5
    }

    def __init__( self ):
        pass

    def baidu_set_data( self, content ):
        if content is None:
            return False
        else:
            product_model = ProductModel()
            # name, status, cycle, yield_rate, threshold, process,
            # type, bank_authority, risk_level, desc, source_url, app_id
            for row in content:
                data = tuple([
                    row["item_name"],
                    1,
                    row["item_duration"],
                    row["e_annualized_rate_of_return"],
                    row["min_purchase_amount"],
                    0, 2, 0,
                    self.risk_level[row["item_risk_level_desc"]],
                    row["an_xin_desc"],
                    row["source_url"],
                    1,
                    row["purchaseLimit"],
                    row["purchase_stop_time"],
                    row["item_id"],
                    row["received_time"]
                ])
                product_model.add_fixed_deposit_list( data )
            return True


    def jd_set_data( self, content ):
        if content is None:
            return False
        else:
            product_model = ProductModel()
            # name, status, cycle, yield_rate, threshold, process,
            # type, bank_authority, risk_level, desc, source_url, app_id
            # item_id, received_time
            for row in content:
                data = tuple([
                    row["itemName"],
                    1,
                    row["investPeriod"],
                    row["itemYield"],
                    ''.join(row["mininvestAmount"].split(',')),
                    0, 2, 0, 2,
                    row["tag"],
                    row["url"],
                    2,
                    "见官网",
                    row["beginInterest"],
                    row["id"],
                    row["tips"]
                ])
                product_model.add_fixed_deposit_list( data )
            return True


    def fh_set_data( self, content ):

        STATUS = {
            "OPENED": 1,
            "FINISHED": 3,
            "SETTLED": 2
        }

        def change_duraton( duration, unit ):
            if unit == u'天':
                return duration
            elif unit == u'个月':
                return int(duration) * 30

        if content is None:
            return False
        else:
            product_model = ProductModel()
            # name, status, cycle, yield_rate, threshold, process,
            # type, bank_authority, risk_level, desc, source_url, app_id
            for row in content:
                data = tuple([
                    row["title"],     # title
                    STATUS[row["status"]],  # status
                    change_duraton(row["duration"], row["durationUnit"]), #cycle
                    row["percentRate"]["displayRate"],   # yield_rate
                    row["minInvestAmount"], # threshold
                    0, 2, 0,  # process, type, bank_authority
                    2, # risk_level
                    row["ctag"], # desc
                    'https://lc.fengjr.com/loan/' + row["id"], # source_url
                    3,  # app_id
                    '见官网',  # limit
                    '', # purchase_stop_time
                    row["id"],   # item_id
                    row["repayMethod"]  # received_time
                ])
                product_model.add_fixed_deposit_list( data )
            return True


    # 公共存储活期数据的方法
    def common_set_huo_data( self, name, yeild, threshold, desc,
        source_url, app_id, item_id, status=1, process=0,
        risk_level=1, bank_authority=0):
        if yeild is None:
            return False
        else:
            product_model = ProductModel()
            data = tuple([name, status, yeild, threshold, process, 1, risk_level, bank_authority, desc, source_url, app_id, item_id])
            product_model.add_current_account_list( data )
            return True

    # 公共存储定期数据的方法
    def common_set_ding_data( self, name, cycle, yeild, threshold,
        desc, source_url, app_id, status=1,
        purchaseLimit=0, purchase_stop_time='', item_id='', received_time='',
        process=0, risk_level=1, bank_authority=0):
        if yeild is None:
            return False
        else:
            product_model = ProductModel()
            data = tuple([name, status, cycle, yeild,
                threshold, process, 2, bank_authority,
                risk_level, desc, source_url, app_id,
                purchaseLimit, purchase_stop_time, item_id, received_time])
            product_model.add_fixed_deposit_list( data )
            return True
