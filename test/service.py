# coding=utf-8
# server.py
from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8000, application)
print "Serving HTTP on port 8000..."
# 开始发送请求
httpd.serve_forever()
