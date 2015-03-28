#!/usr/bin/env python
# -*- coding:utf-8 -*-
from bottle import route, run, template, request
# データ保持
user_list = []

# 192.168.33.10:8080
@route('/hello/', method='GET')
@route('/hello/', method='POST')
def hello():
    user_dict = {}
    user_dict['username'] = request.forms.get('username')
    user_dict['title'] = request.forms.get('title')
    user_dict['body'] = request.forms.get('body')
    user_dict['address'] = request.forms.get('address')

    user_list.append(user_dict)

    return template('hello', user_list=user_list)

run(host='192.168.33.10', port=8080, debug=True, reloader=True)
