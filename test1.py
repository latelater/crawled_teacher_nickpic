# -*- coding:utf-8 -*-
import urllib.request
import re
from bs4 import BeautifulSoup

def getHtml(url):
	headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/535.11 (KHTML, like Gecko) Version/7.0 Mobile/11D257 Safari/535.11'}
	req=urllib.request.Request(url, headers=headers)
	response=urllib.request.urlopen(req)
	contentType = response.headers['Content-Type']
	code = "UTF-8"
	pos = contentType.find('=')
	if -1 != pos:
		code = contentType[pos + 1:len(contentType)]
	the_page1=response.read()
	the_page=the_page1.decode(code, 'ignore')
	return the_page

html = getHtml("http://yjs.njupt.edu.cn/epstar/web/outer/dsfc_ny_.jsp?dsgh=19890007")
soup = BeautifulSoup(html)
print(soup.find('td',bgcolor="#ffffff"))

