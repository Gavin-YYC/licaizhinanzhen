# coding=utf-8
# 首页

from myapp import app
from flask import render_template

@app.route('/')
def hello():
    return render_template('index.html')
