
from httpUtil import *
import requests
import random
import time
import json
from bs4 import BeautifulSoup
import re
from util import *
from config import *

def parseJson(s):
    begin = s.find('{')
    end = s.rfind('}') + 1
    return json.loads(s[begin:end])


def checkStock( skuIds, area):
    # start = int(time.time() * 1000)
    # skuidString = ','.join(skuids)
    if not isinstance(skuIds,list):
        print("skuids必须为list")
    # skuidsStr = ",".join(skuIds)
    skuidsStr= ",".join('%s' % id for id in skuIds)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "https://cart.jd.com/cart.action",
        # "Connection": "keep-alive",
        "Connection": "timeout=60",
        "Host": "c0.3.cn"
    }
    #
    url = 'https://c0.3.cn/stocks'
    payload = {
        'type': 'getstocks',
        'skuIds': skuidsStr,
        'area': area,
        'callback': 'jQuery' + str(random.randint(1000000, 9999999)),
        '_': int(time.time() * 1000),
    }
    resp = requests.get(url=url, params=payload, headers=headers)

    # print(resp.status_code,resp.url)
    inStockSkus = []    # 有货
    notStockSkus = []      # 无货
    disMounts = []      # 下架
    for sku_id, info in parseJson(resp.text).items():
        # print(sku_id,info)
        sku_state = info.get('skuState')  # 商品是否上架
        stock_state = info.get('StockState')  # 商品库存状态
        if sku_state == 1 and stock_state in (33, 40):
            inStockSkus.append(sku_id)       # 有货
        if stock_state == 34:
            notStockSkus.append(sku_id)       # 无货
        if sku_state == 0:
            disMounts.append(sku_id)

    # logger.info('检测[%s]个口罩有货，[%s]个口罩无货，[%s]个口罩下柜，耗时[%s]ms', len(inStockSkuid), len(nohasSkuid), len(unUseSkuid),
    #             int(time.time() * 1000) - start)
    #
    # if len(unUseSkuid) > 0:
    #     logger.info('[%s]口罩已经下柜', ','.join(unUseSkuid))
    return inStockSkus,disMounts

def getSkuHtml(sku):
    url = 'https://item.jd.com/{}.html'.format(sku)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "accept":"accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "connection":"timeout=60"
    }
    html = getPage(url,headers=headers)
    return html

def getSkuName(html):
    soup = BeautifulSoup(html, features='lxml')
    skuNameDiv = soup.find('div', {'class', 'sku-name'})
    skuName = skuNameDiv.text.strip()

    tmp = skuName.split(" ")[:-1]
    skuName= " ".join(tmp)

    return skuName


def getSkuPrice(sku):
    url = 'http://p.3.cn/prices/mgets?skuIds=J_{}'.format(sku)
    j = getJsonData(url,COMMON_HEADERS)

    if j is None:
        return 0
    else:
        return j[0]['p']


def containChinese(check_str):
    for ch in check_str:
        if '\u4e00' <= ch <= '\u9fa5':
            return True
    return False

def getAllSku(html):
    # pattern = re.compile("data-sku=\"(.*?)\".*?data-value=\"(.*?)\"", re.S)
    pattern = re.compile("item.{0,4}data-sku=\"(.*?)\".{0,4}data-value=\"(.*?)\"", re.S)

    matchs = re.findall(pattern,html)
    # print("===========")
    colorAttr = {}
    sizeAttr = {}
    if matchs:
        for match in matchs:
            # print(match)

            # 这一种格式40/7
            # if "/" in match[1]:
            #     match[1] = match[1].split("/")[0]

            if containChinese(match[1]):    # 包含中文
                print(match[1],'中文')
                colorAttr[match[0]] = match[1]
            elif not isNumber(match[1]):    # 都是字母
                print(match[1], '字母')
                colorAttr[match[0]] = match[1]
            else:
                if isNumber(match[1]):   # 正常的尺寸格式
                    # 只收集指定尺寸范围
                    floatSize = float(match[1])
                    #   限制搜索的尺码范围
                    if MIN_SIZE<=floatSize <=MAX_SIZE:
                        sizeAttr[match[0]]=floatSize
                else:
                    sizeAttr[match[0]]=match[1]

    print(colorAttr)
    print(sizeAttr)
    return colorAttr,sizeAttr

def getAllSku_v2(html):
    # print("-----------getAllSku_v2")

    colorAttr = {}
    sizeAttr = {}

    soup = BeautifulSoup(html,features='lxml')

    colorAttrDiv = soup.find('div',id='choose-attr-1')

    if colorAttrDiv:    # 部分只有单属性
        colorAttrDiv = colorAttrDiv.find_all("div",{'class','item'})
        for attr in colorAttrDiv:
            colorAttr[attr['data-sku']]=attr['data-value']

    sizeAttrDiv=soup.find('div',id='choose-attr-2')
    if sizeAttrDiv:
        sizeAttrDiv = sizeAttrDiv.find_all("div",{'class','item'})
        for attr in sizeAttrDiv:
            # print("------------------------")
            # print(attr)
            if isNumber(attr['data-value']):
                floatSize = float(attr['data-value'])
                if MIN_SIZE <= floatSize <= MAX_SIZE:
                    sizeAttr[attr['data-sku']] = floatSize
            else:
                sizeAttr[attr['data-sku']] = attr['data-value']

    # print(colorAttr)
    # print(sizeAttr)
    return colorAttr,sizeAttr

hadOutSkus = []
stackFilePtr = FilePtr('stock/{}.xlsx'.format(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())))

def outputResToFile(sku,html,sizeAttr):
    if sku in hadOutSkus:
        return None
    for skuAttr in sizeAttr:
        hadOutSkus.append(skuAttr)

    if len(sizeAttr)>0:
        # 名字和价格
        skuName = getSkuName(html)
        print(sku, skuName)

        skuPrice = getSkuPrice(sku)
        print(skuPrice)

        # 是否有库存
        skuIds = [sizeSku for sizeSku in sizeAttr.keys()]
        inStockSkus,_ = checkStock(skuIds, AREA)

        for inStockSku in inStockSkus:
            print(inStockSku, sizeAttr[inStockSku])

            stackFilePtr.put(
                {
                    "cate":sku,
                    "sku":inStockSku,
                    "price": skuPrice,
                    "size":sizeAttr[inStockSku],
                    "skuName": skuName,
                    "skuUrl":"https://item.jd.com/{}.html".format(inStockSku),
                }
            )




def getStockRes(sku,mode=1):
    # print(sku)
    print("============================================================扫描下一个sku页面https://item.jd.com/{}.html".format(sku))

    html = getSkuHtml(sku)
    # print("====")
    colorAttr, sizeAttr = getAllSku_v2(html)
    print(colorAttr)
    print(sizeAttr)


    if mode == 1:   #仅获取当前规格的尺码库存
        print('https://item.jd.com/{}.html'.format(sku))
        outputResToFile(sku,html,sizeAttr)
    elif mode==2:   # 获取当前链接下其它的尺码及库存
        if len(colorAttr)>0:
            for sku in colorAttr:
                print('============================================================')
                print('https://item.jd.com/{}.html'.format(sku))
                html = getSkuHtml(sku)
                colorAttr, sizeAttr = getAllSku_v2(html)
                print(colorAttr)
                print(sizeAttr)
                outputResToFile(sku, html, sizeAttr)
        else:
            print("该sku下没有颜色规格")
            outputResToFile(sku, html, sizeAttr)
    else:
        print("SEARCH_MODE 只能是 1 或者 2")
        return None


if __name__=='__main__':
    skuIds = SEARCH_SKUS
    # skuIds = [68418244795,50619335936,40857683328,65585419152,67200535491,59149202098]
    # skuIds = [67200535491,59149202098]
    # skuIds = [68266755089]
    # skuIds = [40857683328]
    for sku in skuIds:
        getStockRes(sku,mode=SEARCH_MODE)

    stackFilePtr.close()