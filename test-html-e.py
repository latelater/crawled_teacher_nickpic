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

# print(html)
soup = BeautifulSoup(html,"html.parser")
# print(soup.prettify())

#print(soup.head,"html.parser")
# print(soup.p.parent)
print(soup.find('td',bgcolor="#ffffff"))
#print(soup.find(text="研究方向及主要成果").parent)
#print(soup.find('font').string)
name = soup.find('font').string
text = re.findall(r'<TD bgColor="#ffffff" align="center">.*</TD>',html)
#text1 = soup.find_all('td',bgcolor="#ffffff")
text2 = soup.find_all('td', {'bgColor': '#ffffff'})
text3 = re.findall(r'<P align="left">.*</P>',html)
#print(name)
print(text)
print(text2)
print(text3)


#print(soup.find("a",text="Elsie").parent)
