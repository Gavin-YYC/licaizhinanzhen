# coding=utf-8
import MySQLdb
from flask import g
def sql_install( app ):
    from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
        MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
    )

    @app.before_request
    def before_request():
        g.db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASS,
                               MYSQL_DB, port=int(MYSQL_PORT), charset = 'utf8')

    @app.teardown_request
    def teardown_request(exception):
        if hasattr(g, 'db'): g.db.close()

