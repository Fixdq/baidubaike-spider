#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-26 上午11:33
# @Author  : fixdq
# @File    : spider_main.py
# @Software: PyCharm
from baike import url_manager, html_downloader, html_parser, html_outputer
import ssl

class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url:
            try:
                new_url = self.urls.get_new_url()
                print('craw %s : %s' % (count, new_url))
                html_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parser(new_url, html_cont)
                self.urls.add_new_urls(new_urls)
                self.outputer.clooect_data(new_data)
                count += 1
                if count == 10:
                    break
            except:
                print('craw failed')
        self.outputer.out_put_html()


if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python/407313'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
