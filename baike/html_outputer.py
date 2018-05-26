#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-26 上午11:34
# @Author  : fixdq
# @File    : html_outputer.py
# @Software: PyCharm
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def clooect_data(self, data):
        if not data:
            return
        self.datas.append(data)

    def out_put_html(self):
        with open('/home/fixd/Desktop/res.html','w') as f:
            # 将
            f.write('<html>')
            f.write('<head>')
            f.write('<meta charset="utf-8">')
            f.write('</head>')
            f.write('<body>')
            f.write('<table>')

            for data in self.datas:
                f.write('<tr>')
                f.write('<td>%s</td>' % data['url'])
                f.write('<td>%s</td>' % data['title'])
                # f.write('<td>%s</td>' % data['summary'])
                f.write('</tr>')

            f.write('</table>')
            f.write('</body>')
            f.write('</html>')