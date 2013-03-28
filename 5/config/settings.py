#!/usr/bin/env python
# coding: utf-8
import web
import sae.const
#数据库设定
db = web.database(dbn='mysql', user=sae.const.MYSQL_USER, pw=sae.const.MYSQL_PASS, host=sae.const.MYSQL_HOST, port=3307,
                  db=sae.const.MYSQL_DB)
#模板设定
render = web.template.render('templates/', cache=False)

config = web.storage(
    email='oooo@qq.com',
    site_name='任务跟踪',
    site_desc='',
    static='/static',
)

web.template.Template.globals['config'] = config
web.template.Template.globals['render'] = render

