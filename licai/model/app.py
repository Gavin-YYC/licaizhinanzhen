# coding=utf-8

from flask import g

class AppModel( object ):

    # 新闻表
    news_table_name = 'product_news'
    # app表
    app_table_name = 'product_app'

    def __init__( self ):
        pass

    # 获取活期存款列表
    def get_app_list( self ):
        c = g.db.cursor()
        c.execute("SELECT id, name, icon_src, online_at, home FROM product_app")
        res_all = c.fetchall()
        res = self.to_dict_app(res_all)
        for row in res:
            c.execute("SELECT id, title, link, date FROM product_news WHERE app_id={0} ORDER BY date DESC".format(row["id"]))
            news_res_all = c.fetchall()
            news_res = self.to_dict_news(news_res_all)
            row["news"] = news_res
        return res

    def to_dict_app( self, content ):
        if content is None:
            return None
        else:
            res = []
            for row in content:
                print row
                id, name, icon_src, online_at, home = row
                res.append({
                	"id": id,
                    "name": name,
                    "icon_src": icon_src,
                    "online_at": online_at,
                    "home": home,
                    "news": []
                })
            return res

    def to_dict_news( self, content ):
        if content is None:
            return None
        else:
            res = []
            for row in content:
                print row
                id, title, link, date = row
                res.append({
                	"id": id,
                    "title": title,
                    "link": link,
                    "date": date
                })
            return res
