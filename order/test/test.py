import random
import re

import requests
import time
import json
from util import *
from datetime import datetime
from datetime import date


from pageInfo import *
from util import  *
from bs4 import BeautifulSoup

def testGetColorSize():
    url = 'https://item.jd.com/20335974678.html'   # 正常 {'color': 'C77124-19冬季', 'size': '36.5'}
    url = 'https://item.jd.com/65585419154.html'   # 只有一个 {'color': ' ', 'size': '42'}
    url = 'https://item.jd.com/100011551632.html'  # 下架 {'color': ' ', 'size': ' '}
    url = 'https://item.jd.com/6571612.html'       # 无规格选项商品 {'color': ' ', 'size': ' '}

    print(getColorSize(url))



def testGetShopName():
    cookieDict = getCookieDict("../cookie")

    cookie = cookieDict["a13218343010"]

    # 店铺名
    shopName = 62629
    print(getShopName(shopName, cookie))

START_TIME = "2020-05-01 00:00:00"
END_TIME = "2020-05-04 23:59:59"
def testTime(timeList):
    for time in timeList:
        if START_TIME<=time<=END_TIME:
            print(time,"True")
        else:
            print(time,"False")


def testGetNextPage():
    cookie = getCookieDict('../cookie')['a13218343010']

    # 第三方
    url ='https://details.jd.com/normal/item.action?orderid=113760549393&PassKey=A02A1E4B30F6E722A8B6FE49490A15F9'
    # 京东自营
    # url = 'https://details.jd.com/normal/item.action?orderid=113879539065&PassKey=7057B83D753E5F0EF8F0551478DD2C41'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'referer': 'https://order.jd.com/center/list.action',
        'cookie': cookie
    }
    html = getPage(url,headers)



    pattern = re.compile("class=\"p-info.*?p-name.*?item.jd.com/(.*?).html"    # sku
                         ".*?a-link.*?title=\"(.*?)\">"         # 商品简略信息
                         ".*?f-price\".*?<td>(.*?)</td>"    # 单价
                         ,re.S)

    matchs = re.findall(pattern,html)

    if matchs:
        for match in matchs:
            print(match[0].strip())
            # print(match[1])
            # print(match[2])

    soup = BeautifulSoup(html,features='lxml')
    panel = soup.find('div',{'class','ui-switchable-panel'})
    dd = panel.find('div',{'class','dd'})
    info = dd.find_all('div',{'class','info-rcol'})

    print("-----")
    print(info[0].text.strip())
    print(info[2].text.strip())
    # for i in info:
    #     print("-----")
    #     print(i.text.strip())

def testDesc():
    # str = '李宁官方篮球鞋男鞋闪击VIpremium男子一体织减震支撑中帮鞋专业比赛鞋ABAP071 烟玫瑰粉/风沙粉-5 40'
    str ='阿迪达斯官网 adidas COURT80S MID男女鞋网球运动鞋EE9678 如图 43'

    size = str.split(" ")[-1]

    print(isNumber(size),len(size),size)

    matchs = re.findall("(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{5,10}",str)
    if matchs:
        for match in matchs:
            print(match)


if __name__=='__main__':

    # testGetShopName()

    # testGetColorSize()
    # timeList = ['2020-04-29 19:07:52','2020-05-02 00:31:21','2020-05-05 17:03:53']
    # testTime(timeList)

    # print(getColor())

    print(random.randint(40,60)*0.01)

    # testGetNextPage()

