﻿import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import time
  
  
def get_one_page(all_url):
    '''获取单个页面的HTML文本'''
    try:
        response = requests.get(all_url,timeout=20)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        #print(response.text)
        return response.text
    except:
        print('Failed')
        return None
  
  
def parse_all_pages(html,urls,chapter_name):
    '''解析章节信息并存入列表'''
    soup = BeautifulSoup(html,'html.parser')
    #soup = BeautifulSoup(html.text)
    chapters = soup.find('div',class_='listmain')
    #print(chapters)
    for dd in chapters.find_all('a')[12:]:
        urls.append(dd.get('href'))
        chapter_name.append(dd.text)
  
  
def parse_one_chapter(content):
    '''解析并返回章节内容'''
    soup = BeautifulSoup(content,'html.parser')
    #title = soup.find('div',class_='content').find('h1').text
    texts = soup.find_all('div',class_='showtxt')[0].text.replace('\xa0'*8,'\n\n')
    print(texts)
    return texts
  
  
def write_to_file(chapter_name,texts):
    '''将章节内容写入txt文件'''
    with open ('《家有冥妻》.txt','a',encoding='utf-8') as f:
        f.write(chapter_name + '\n')
        f.write(texts)
        f.write('\n\n')
  
  
def main():
    urls = [] # 存放链接的列表
    chapter_name = [] # 存放章节名称的列表
    all_url = 'https://www.biqukan.com/0_104/'
    html = get_one_page(all_url)
    parse_all_pages(html,urls,chapter_name)
    print('《家有冥妻》开始下载。。。')
    print(range(len(chapter_name)))
    for i in range(len(chapter_name)):
        url = 'http://www.biqukan.com'+ urls[i]
        content = get_one_page(url)
        texts = parse_one_chapter(content)
        #write_to_file(chapter_name[i],texts)
        time.sleep(1)
    print('《家有冥妻》下载完成。。。')
  
  
if __name__ == '__main__':
    main()