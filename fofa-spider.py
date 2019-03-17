# coding:utf-8
import os
import sys
import requests
import tableprint
from config import *
from requests_html import HTMLSession
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def task(url):
    creat_txt()
    session = HTMLSession()
    for pages in range(1,1001):
        print(define.GREEN+"[*]current page : %s"%pages)
        try:
            r = session.get(url+'&page=%s'%pages,headers=define.headers,verify=False,timeout=define.Timeout)
        except Exception as e:
            print(define.RED+e)
        try:
            for i in range(2,12):
                ip = r.html.xpath('//*[@id="ajax_content"]/div/div[%s]/div[1]/a/text()'%i)[0]
                try:
                    title = str(r.html.xpath('//*[@id="ajax_content"]/div/div[%s]/div[2]/div/div[1]/ul/li[1]/text()'%i)).split('            ')[1].strip('''']''')
                except IndexError as e:
                    title = 'None'
                with open(define.filename,'a+',encoding='utf-8') as f:
                    f.write(ip.strip()+'^'+title+'\n')
                print(define.GREEN+'[*]当前抓取 ' + str(ip) + ' : ' + title)
        except IndexError as e:
            break
    print(define.BLUE+"[*]任务执行完毕 文件保存为:%s"%define.filename)

def creat_txt():
    if os.path.exists(define.filename) == False:
        if os.path.exists('out/') == False:
            os.mkdir('out')
        with open(define.filename,'a+',encoding='utf-8') as a:
            print(define.BLUE+"[*]创建文件成功 %s"%define.filename)
    else:
        print(define.RED+"[*]文件已存在 文件为:%s"%define.filename)

if __name__ == '__main__':
    print(define.ORANGE+define.banner)
    if len(sys.argv) < 2:
        print(define.ORANGE+define.usage)
    elif sys.argv[1] == '-u':
        try:
            print(define.BLUE+"[*]开始抓取")
            task(str(sys.argv[2]))
            print(define.BLUE+"[*]抓取完毕")
        except:
            print(define.RED+'[*]Something went wrong')
    else:
        print(define.ORANGE+define.usage)
