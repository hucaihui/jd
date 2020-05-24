import requests

import os
import re
from util import *
import time
import json
import pandas as pd
from config import *
import random
from config import *
import json
from httpUtil import *




# 获取物流信息及物流号
def getTraceInfo(orderId,cookie):
    data = {
        'orderId': str(orderId),
        'orderType': '22',
        'orderStatus': '15',
        'orderStoreId': '0',
        'pickDate': str(int(time.time() * 1000))
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'accept':'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': cookie
    }

    url = 'https://details.jd.com/lazy/getOrderTrackInfoMultiPackage.action'

    resp=requests.post(url,data=data,headers=headers)
    content=resp.text

    try:
        if content is not None:
            j = json.loads(content)

            carriageIds = ""
            carriers = ""
            isOne = False
            for trackInfo in j["multiPackageTrackInfoList"]:
                if isOne:
                    carriageIds = trackInfo['carriageInfo']['carriageId'] + "/"+carriageIds
                    carriers =trackInfo['carriageInfo']['carrier'] +"/"+carriers

                else:
                    carriageIds = trackInfo['carriageInfo']['carriageId']
                    carriers = trackInfo['carriageInfo']['carrier']
                    isOne = True
                # print(trackInfo['carriageInfo']['carriageId'], trackInfo['carriageInfo']['carrier'])
            return {"carriageId":carriageIds,
                    "carrier":carriers
                    }
    except Exception as e:
        print(e)
        # print(orderId+" 无物流")
        return {"carriageId":"无物流",
                "carrier":"无物流"
                }

# 获取店铺名字
def getShopName(shopNo,cookie):

    retObj = getJsonData(PRE_URL+"/shop/selectOne?id={}".format(shopNo))
    # print(retObj)
    if retObj is not None :
        if retObj['success']:
            return retObj['obj']['shopNo']

    url = 'https://details.jd.com/lazy/getPopTelInfo.action'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'content-type': 'application/x-www-form-urlencoded',
        # 'refer':'https://details.jd.com/normal/item.action',
        'cookie': cookie
    }
    data={
        'popVenderIds': str(shopNo)
    }
    resp = requests.post(url,data=data,headers=headers)
    context = resp.text
    # print(resp.status_code,context)
    try:
        if context is not None:
            j = json.loads(context)
            shopName =j[str(shopNo)]['venderName']

            if not postJsonData(PRE_URL + "/shop/insert", {'shopNo':shopNo,'shopName':shopName}):
                print("shopName存入数据库失败：", {'shopNo':shopNo,'shopName':shopName})
            return shopName

    except Exception as e:
        print(e)
        return "venderId:"+shopNo


# 获取商品规格和尺寸
def getColorSize(sku,desc):
    colorSize = {
        "sku":str(sku),
        "descInfo":str(desc),
        "articleNo":" ",
        "color": " ",
        "size": " "
    }

    retObj = getJsonData(PRE_URL+"/goods/selectOne?id={}".format(sku))
    if retObj is not None :
        if retObj['success']:
            colorSize['articleNo'] = retObj['obj']['articleNo']
            colorSize['color'] = retObj['obj']['color']
            colorSize['size'] = retObj['obj']['size']

            return colorSize


    skuUrl = 'https://item.jd.com/{}.html'.format(sku)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    }

    html = getPage(skuUrl,headers=headers)
    if html:
        #货号
        matchsArticleNo = re.search("货号：(.*?)<",html)    # 货号 Article No
        if matchsArticleNo:
            colorSize['articleNo']=matchsArticleNo.group(1)

        # 颜色
        patternColor1 = re.compile("choose-attr-1.*?selected.*?"
                             "data-value=\"(.*?)\">",    # 颜色 /规格
                             re.S)
        matchsColor1 = re.search(patternColor1,html)
        if matchsColor1:
            colorSize['color']= matchsColor1.group(1)

        # 尺寸
        patternSize =re.compile("choose-attr-2.*?selected.*?"
                             "data-value=\"(.*?)\">",   # 尺寸
                             re.S)
        matchSize = re.search(patternSize, html)
        if matchSize:
            colorSize['size'] = matchSize.group(1)
        else:
            # 从desc中提取尺寸
            size = desc.split(" ")[-1]
            if isNumber(size) or len(size) == 1:
                colorSize['size'] = '*' + size


        # 存入数据库
        if  not postJsonData(PRE_URL+"/goods/insert",colorSize):
            print("colorSize存入数据库失败：",colorSize)

    else:
        colorSize['articleNo'] = '请求{}失败'.format(skuUrl)

    return colorSize