# -*- coding: utf-8 -*-

# test.py
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

html = html.replace(u'\xa0', u'')
soup = BeautifulSoup(html, "html.parser")

print(soup.find('font', color='#333333').string[:-2])

# print(soup.find_all('td', bgcolor="#ffffff"))
# print(soup.find(text='个人简介').parent.parent.next_sibling.next_sibling)
# print(soup.find(text='研究方向及主要成果').parent.parent.next_sibling.next_sibling)

print(re.findall(r'Email.*', soup.prettify())[0].replace(u'\xa0', u''))

profile = soup.find_all('td', bgcolor='#ffffff')
for index in range(len(profile)):
	if index % 2 == 0:
		strong = profile[index].find('strong')
		if strong is not None:
			print(strong.string)
	else:
		print(profile[index].string)

print('个人简介')
person = soup.find(text='个人简介').parent.parent.next_sibling.next_sibling
for child in person.children:
	print(child)

print('研究方向及主要成果')
result = soup.find(text='研究方向及主要成果').parent.parent.next_sibling.next_sibling
for child in result.children:
	print(child)
