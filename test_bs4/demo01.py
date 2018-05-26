#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 18-5-26 上午10:00
# @Author  : fixdq
# @File    : demo01.py
# @Software: PyCharm

from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'lxml')
print(soup.tag_name_re)
print(soup.title)
print(soup.name)
print(soup.head)
print(soup.head.name)
print(soup.head.attrs)
print(soup.a)
print(soup.a.attrs)
# print(soup.prettify())
res = soup.find_all('a')

for re in res:
    print(re.name, re['href'], re.text)
res1 = soup.find('a', href='http://example.com/elsie')
# for re in res1:
print(res1.name, res1['href'], res1.get_text())


