# coding=utf-8
import os
from flask import Flask, g, request, render_template
from werkzeug.wsgi import SharedDataMiddleware
from sql import sql_install

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))

# 初始化应用
app = Flask(
    __name__,
    template_folder=os.path.join(project_path, 'static')
)

app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
        '/': os.path.join(project_path, 'static')
    })

# 调试模式
app.debug = True

# 数据库
sql_install( app )

from api import *
