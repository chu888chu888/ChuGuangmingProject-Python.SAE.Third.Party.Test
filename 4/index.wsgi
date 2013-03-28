#!/usr/bin/env python
# coding: utf-8
import os
import sys
import web
import sae
from config.url import urls
from config import settings

app_root = os.path.dirname(__file__)

# 两者取其一
sys.path.insert(0, os.path.join(app_root, 'virtualenv.bundle'))
#是否具有调试功能
web.config.debug = True
# app = web.application(urls, globals()).wsgifunc()
# application = sae.create_wsgi_app(app)

#解决Session在SAE中的问题
app = web.application(urls, globals())

#将session保存在数据库中
db = settings.db
store = web.session.DBStore(db, 'sessions')
#session = web.session.Session(app, store, initializer={'access_token': 'true'})
session = web.session.Session(app, store)
web.config._session = session

application = sae.create_wsgi_app(app.wsgifunc())


