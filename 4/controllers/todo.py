#!/usr/bin/env python
# coding: utf-8

import Queue
from urllib import FancyURLopener

from config import settings

render = settings.render


class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/534.55.3 (KHTML, like Gecko) Version/5.1.3 Safari/534.53.10'


class Spider:
    def get_html(self, url):
        myopener = MyOpener()
        sock = myopener.open(url)
        htmlSource = sock.read()
        sock.close()
        return htmlSource

    def analysis_html(self, htmlSource):
        import lxml.html.soupparser as soupparser
        #htmlSource = unicode(htmlSource, 'utf-8', errors='ignore')
        dom = soupparser.fromstring(htmlSource)
        Url = dom.xpath('//*[@id="RecentBlogs"]/ul[1]/li/div/h3/a[@href]')
        title = dom.xpath('//*[@id="RecentBlogs"]/ul[1]/li/div/h3/a/text()')
        writer = dom.xpath('//*[@id="RecentBlogs"]/ul[1]/li/div/div/text()')
        for i in range(len(title)):
            print title[i].encode('utf-8'), Url[i].get('href').encode('utf-8'), writer[i].encode('utf-8')


class Index:
    def GET(self):

        spider = Spider()
        url = ['http://www.oschina.net/blog/more?p=%s#' % (i) for i in range(10)]
        urls = Queue.Queue()

        for i in url:
            urls.put(i)
        for i in range(urls.qsize()):
            url = urls.get()
            htmlSource = spider.get_html(url)
        return htmlSource

