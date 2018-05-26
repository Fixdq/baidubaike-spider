#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-26 上午11:33
# @Author  : fixdq
# @File    : html_downloader.py
# @Software: PyCharm
from urllib import request


class HtmlDownloader(object):

    def download(self, url):
        if not url:
            return None

        # response = request.urlopen(url)
        response = request.urlopen(url)
        if response.getcode() != 200:
            return None
        return response.read()
