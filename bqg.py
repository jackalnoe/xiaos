#-*- coding:utf-8 -*-
import urllib.request
import re
import requests
from bs4 import BeautifulSoup
from lxml import etree
import datetime 


#得到前一天的日期
i = (datetime.datetime.now() - datetime.timedelta(days = 1)) 
#输出日期格式为201913
#date = "%s-%s" % (i.month,i.day)
date = i.strftime("%m-%d")
print(date)
def get_index():
	url='https://www.biqukan.com/0_104/'#页数的url地址
	html=urllib.request.urlopen(url).read()#读取首页的内容
	selector=etree.HTML(html)#转换为xml，用于在接下来识别
	#links=selector.xpath('//*[@id="tab_con1"]/div/ol/li[1]/a/text()')#抓取当前页面的所有帖子的url
	link=selector.xpath('/html/body/div[5]/dl/a/@href')
	#links.remove('https://m.xwlbo.com/');#从清单中删除含有https://m.xwlbo.com/的内容

	print(link)

	
	

get_index()


