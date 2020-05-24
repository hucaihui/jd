
import requests
import os
import re
from util import *
import time
import json
import pandas as pd
from config import *
import random

from pageInfo import *
from bs4 import BeautifulSoup



# 解析订单详情
def parseNextPage(fileName,orderId,url,cookie):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'referer': 'https://order.jd.com/center/list.action',
        'cookie': cookie
    }
    html = getPage(url,headers)
    # print(html)

    pattern = re.compile("class=\"p-info.*?p-name.*?item.jd.com/(.*?).html"    # sku
                         ".*?a-link.*?title=\"(.*?)\">"         # 商品简略信息
                         ".*?f-price\".*?<td>(.*?)</td>"    # 单价
                         ,re.S)

    matchs = re.findall(pattern,html)

    if matchs:
        shopNo = re.findall('venderId\".*?value=\"(.*?)\"',html)
        # print(shopNo)
        shopName = "京东"                                   # 店铺名
        if '0'!=shopNo[0]:
            shopName = getShopName(shopNo[0],cookie)

        totalMoney = re.findall('count">&yen;(.*?)<',html)    # 订单总金额
        # print(shopName,totalMoney)
        try:
            if float(totalMoney[0].strip())<MIN_MONEY:
                msg ="小于 {} 金额的订单不导出,该订单总金额：{}".format(MIN_MONEY,totalMoney[0])
                print(msg)
                return msg
        except Exception as e:
            print("该字符串无法转为数字：",totalMoney[0].strip())
            print(e)

        trace = getTraceInfo(orderId,cookie)                # 订单物流信息

        print(orderId, shopName, totalMoney, trace)

        # 收货人信息
        soup = BeautifulSoup(html, features='lxml')
        panel = soup.find('div', {'class', 'ui-switchable-panel'})
        dd = panel.find('div', {'class', 'dd'})
        info = dd.find_all('div', {'class', 'info-rcol'})

        consignee = info[0].text.strip()         # 收货人
        phone = info[2].text.strip()     # 收货地址

        for match in matchs:
            # print(match
            sku =match[0]           # sku,
            desc = match[1]         # 商品简信
            goodsNum = match[2]     # 数量

            print(sku,desc,goodsNum)

            colorSize = getColorSize(sku,desc)



            # 写入缓冲
            global  orderTime
            content={
                "orderId":orderId,
                "orderTime":orderTime,
                "shopName":shopName,
                "totalMoney":totalMoney,
                "consignee":consignee,
                "phone":phone,
                "sku":sku,
                "articleNo":colorSize['articleNo'],
                "color":colorSize['color'],
                "size":colorSize['size'],
                "goodsNum": goodsNum,
                "carriageId":trace['carriageId'],
                "carrier:":trace['carrier'],
                "desc":desc

            }
            # fileName = "xls/"+userName+".xlsx"
            filePtr = getFilePtr(fileName)
            filePtr.put(content)



# 获取订单号
def parseOnePage(fileName,cookie,d,page):
    time.sleep(0.5)

    url = 'https://order.jd.com/center/list.action?d={}&s=4096&t=0-6-8-9-10-11-13-15-16-17-18-19-21-22-23-24-25-32-33-41-42-49-54-56-112&page={}'\
        .format(d,page)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>当前页码".format(page))
    print(url)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'cookie': cookie
    }

    html = getPage(url,headers)
    # print(html)

    pattern = re.compile("dealtime\".*?>(.*?)</span.*?name='orderIdLinks"   # 下单时间
                         ".*?href='(.*?)'"            # 订单详情链接 
                         ".*?>(.*?)</a>"               # 订单号
    
                         ".*?order-status.*?>(.*?)</span>"    # 订单状态
                         ,re.S)
    matchs = re.findall(pattern,html)
    if matchs:
        for match in matchs:

            orderState = match[3]   # 订单状态
            if '已取消' in orderState:
                continue

            global orderTime
            orderTime = match[0]   #订单时间
            if orderTime>END_TIME:   # 先扫描的是大时间的
                continue
            if orderTime<START_TIME :    # 指定时间范围
                break
            print("=============================")
            # print('url:',url)
            # print(match)
            print(match[0],match[2],match[3].strip())

            nextUrl = 'https:'+match[1]    # 订单详情链接

            print('page:',page,' url:',nextUrl)
            # nextUrl = 'https://details.jd.com/normal/item.action?orderid=120142536096&PassKey=4FF7D51E42B27F1B1459BD7D88BEEE6D'
            # random.randint(4,6)*0.1
            time.sleep(random.randint(40,60)*0.01)
            parseNextPage(fileName,match[2],nextUrl,cookie)
            # break




if __name__=='__main__':
    cookieDict = getCookieDict("cookie")

    for userName in cookieDict.keys():
        cookie = cookieDict[userName]
        fileName = "xls/"+userName+".xlsx"

        d = D
        pageNum = 5
        for page in range(pageNum):
            parseOnePage(fileName,cookie,d,page+1)

    # 缓存保存
        saveToFile(fileName)