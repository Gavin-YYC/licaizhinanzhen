# coding=utf-8

from flask import g

class ProductModel( object ):

    # 活期存款表
    current_account_table_name = 'product_current_account'
	# 定期存款表
    fixed_deposit_table_name = 'product_fixed_deposit'

    # app表
    app_table_name = 'product_app'


    # 获取活期存款列表
    def get_current_account_list( self, p_type, p_status, p_threshold, p_yield_rate, p_risk_level, p_process, p_bank_deposit ):
        c = g.db.cursor()
        c.execute("SELECT {table_name}.*, {app_table_name}.name, {app_table_name}.icon_src FROM {table_name}, {app_table_name} WHERE \
        	type={p_type} AND \
            status={status} AND \
            threshold>={threshold[0]} AND \
            threshold<={threshold[1]} AND \
            yield_rate>={yield_rate[0]} AND \
            yield_rate<={yield_rate[1]} AND \
            risk_level>={p_risk_level[0]} AND \
            risk_level<={p_risk_level[1]} AND \
            bank_authority={bank_authority} AND \
            process>={process[0]} AND \
            process<={process[1]} AND \
            {table_name}.app_id = {app_table_name}.id \
            ORDER BY yield_rate DESC LIMIT 0, 10".format(
            	table_name=self.current_account_table_name,
            	app_table_name = self.app_table_name,
            	p_type = p_type,
            	status = p_status,
            	threshold = p_threshold,
            	yield_rate = p_yield_rate,
            	p_risk_level = p_risk_level,
            	bank_authority = p_bank_deposit,
            	process = p_process
        	))
        res_all = c.fetchall()
        res = self.to_dict(res_all)
        return res


    # 获取定期存款列表
    def get_fixed_deposit_list( self, p_type, p_status, p_threshold, p_yield_rate, p_cycle, p_risk_level, p_process, p_bank_deposit ):
        c = g.db.cursor()
        c.execute("SELECT {table_name}.*, {app_table_name}.name, {app_table_name}.icon_src FROM {table_name}, {app_table_name} WHERE \
        	type={p_type} AND \
            status={status} AND \
            threshold>={threshold[0]} AND \
            threshold<={threshold[1]} AND \
            cycle>={cycle[0]} AND \
            cycle<={cycle[1]} AND \
            yield_rate>={yield_rate[0]} AND \
            yield_rate<={yield_rate[1]} AND \
            risk_level>={p_risk_level[0]} AND \
            risk_level<={p_risk_level[1]} AND \
            bank_authority={bank_authority} AND \
            process>={process[0]} AND \
            process<={process[1]} AND \
            {table_name}.app_id = {app_table_name}.id \
            ORDER BY yield_rate DESC LIMIT 0, 10".format(
            	table_name=self.fixed_deposit_table_name,
            	app_table_name = self.app_table_name,
            	p_type = p_type,
            	status = p_status,
            	threshold = p_threshold,
            	cycle = p_cycle,
            	yield_rate = p_yield_rate,
            	p_risk_level = p_risk_level,
            	bank_authority = p_bank_deposit,
            	process = p_process
        	))
        res_all = c.fetchall()
        res = self.to_dict_2(res_all)
        return res




    def to_dict( self, content ):
        if content is None:
            return None
        else:
            res = []
            for row in content:
                id, name, status, yield_rate, \
                threshold, process, type, risk_level, \
                bank_authority, p_desc, source_url, app_id, item_id, app_name, app_icon_src = row
                res.append({
                	"id": id,
                    "name": name,
                    "type": type,
                    "status": status,
                    "threshold": threshold,
                    "yield_rate": yield_rate,
                    "risk_level": risk_level,
                    "bank_authority": bank_authority,
                    "process": process,
                    "desc": p_desc,
                    "source_url": source_url,
                    "app_name": app_name,
                    "app_icon_src": app_icon_src
                })
            return res

    def to_dict_2( self, content ):
        if content is None:
            return None
        else:
            res = []
            for row in content:
                id, name, status, cycle, yield_rate, \
                threshold, process, type, risk_level, \
                bank_authority, p_desc, source_url, app_id, \
                purchase_limit, purchase_stop_time, item_id, \
                received_time, app_name, app_icon_src = row
                res.append({
                	"id": id,
                    "name": name,
                    "type": type,
                    "status": status,
                    "cycle": cycle,
                    "threshold": threshold,
                    "yield_rate": yield_rate,
                    "risk_level": risk_level,
                    "bank_authority": bank_authority,
                    "process": process,
                    "desc": p_desc,
                    "source_url": source_url,
                    "purchase_limit": purchase_limit,
                    "purchase_stop_time": purchase_stop_time,
                    "app_name": app_name,
                    "app_icon_src": app_icon_src
                })
            return res


    def add_fixed_deposit_list( self, content ):
        c = g.db.cursor()
        try:
            a_sql = "SELECT * FROM product_fixed_deposit WHERE item_id='{0}'".format(content[14])
            hisRes = c.execute(a_sql)
            res = c.fetchone()
            # 没有时，添加该数据
            if res is None:
                sql = "INSERT INTO product_fixed_deposit (name, status, cycle, yield_rate, \
                    threshold, process, type, bank_authority, risk_level, \
                    p_desc, source_url, app_id, purchase_limit, purchase_stop_time, \
                    item_id, received_time ) VALUES (%s, %s, %s, %s, %s, %s, \
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                c.execute(sql, content)
            # 存在时，修改该数据
            else:
                cur_id = res[0]
                sql = "UPDATE product_fixed_deposit SET name='{content[0]}', status={content[1]}, cycle={content[2]}, \
                    yield_rate={content[3]}, threshold={content[4]}, process={content[5]}, type={content[6]}, \
                    bank_authority={content[7]}, risk_level={content[8]}, p_desc='{content[9]}', \
                    source_url='{content[10]}', app_id={content[11]}, purchase_limit='{content[12]}', \
                    purchase_stop_time='{content[13]}', item_id='{content[14]}', \
                    received_time='{content[15]}' WHERE id={cur_id}".format(content=content, cur_id=cur_id)
                c.execute(sql)
            g.db.commit()
            return True
        except:
            g.db.rollback()
            return False


    def add_current_account_list( self, content ):
        c = g.db.cursor()
        try:
            hisRes = c.execute("SELECT * FROM product_current_account WHERE item_id='{0}'".format(content[11]))
            res = c.fetchone()
            # 没有时，添加该数据
            if res is None:
                sql = "INSERT INTO product_current_account (name, status, yield_rate, \
                    threshold, process, type, risk_level, bank_authority, \
                    p_desc, source_url, app_id, item_id ) VALUES (%s, %s, %s, %s, %s, %s, \
                    %s, %s, %s, %s, %s, %s)"
                c.execute(sql, content)
            # 存在时，修改该数据
            else:
                cur_id = res[0]
                sql = "UPDATE product_current_account SET name='{content[0]}', status={content[1]}, \
                    yield_rate={content[2]}, threshold={content[3]}, process={content[4]}, type={content[5]}, \
                    risk_level={content[6]}, bank_authority={content[7]}, p_desc='{content[8]}', \
                    source_url='{content[9]}', app_id={content[10]} WHERE id={cur_id}".format(content=content, cur_id=cur_id)
                c.execute(sql)
            g.db.commit()
            return True
        except:
            g.db.rollback()
            return False
