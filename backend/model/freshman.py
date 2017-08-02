# coding=utf-8

from flask import g

class FreshmanModel( object ):

    table_name = 'freshman'

    def get_freshman_list( self ):
        c = g.db.cursor()
        c.execute("select id, name, icon, base_yields, time_long, min_invest, home_url from {0}".format(self.table_name))
        res = list(c.fetchall())
        output = []
        for index in range(len(res)):
            output.append({
                'id': res[index][0],
                'name': res[index][1],
                'icon': res[index][2],
                'base_yields': res[index][3],
                'time_long': res[index][4],
                'min_invest': res[index][5],
                'home_url': res[index][6]
            })
        return output
