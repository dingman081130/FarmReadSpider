#!/usr/bin/env python
#coding=utf8

from urllib2 import urlopen
from urllib import urlencode
from urllib import quote
from lxml.html import parse

stories = [
        '桃园结义',
        '割发代首',
        ]

print 'Start ...'

url = 'http://baike.baidu.com/search/word?word=%E5%89%B2%E5%8F%91%E4%BB%A3%E9%A6%96&pic=1&sug=1&enc=utf8&rsp=%5Bobject+Object%5D'

page = urlopen(url)

print parse(page).xpath("string()")

#print url
#for story in stories:
#    print story
#    print quote(story)
