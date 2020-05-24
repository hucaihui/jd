from time import sleep

from stock import *
from config import *
import requests




def sendWeChat(text,desp=None):
    if SCKEY == " ":
        return

    if desp is None:
        sendUrl = "https://sc.ftqq.com/{}.send?text={".format(
           SCKEY,text
        )
    else:
        sendUrl = "https://sc.ftqq.com/{}.send?text={}&desp={}".format(
           SCKEY,text,desp
        )
    resp = requests.get(sendUrl)
    # print(resp.url)

skuDict = {}
hadStockSku = []
def monitor(skuIds,monitorMode=1):
    searchSkuIds = []
    if monitorMode == 1 :   # 仅监控当前sku
        searchSkuIds = skuIds
    elif monitorMode == 2:   # 搜索所有尺码
        for sku in skuIds:
            html = getSkuHtml(sku)
            colorAttr, sizeAttr = getAllSku_v2(html)
            for tmp in sizeAttr:
                searchSkuIds.append(tmp)
    else:
        print("MONITOR_MODE 值只能是1或者2")
        return None


    for sku in searchSkuIds:

        html = getSkuHtml(sku)
        skuName = getSkuName(html)
        colorAttr, sizeAttr = getAllSku_v2(html)

        skuDict[sku] = {
            "sku":sku,
            "size":sizeAttr[sku],
            "skuName":skuName,
        }

    countTime = 0
    while True:
        inStockSkus,disMounts=checkStock(searchSkuIds,AREA)

        text = " "
        desp = " "
        for inStockSku in inStockSkus:
            hadStockSku.append(inStockSku)   # 已经有了的放弃监控
            searchSkuIds.remove(inStockSku)

            print("=========================================================")
            print("{}到货".format(inStockSku), skuDict[inStockSku])

            text += "{}—".format(inStockSku)
            info = skuDict[inStockSku]
            desp += "https://item.jd.com/{}.html ——{}——" \
                    "{}/——————————————————————————————/".format(inStockSku, info['size'], info['skuName'])

        if len(inStockSkus)>0:
            # 相同信息限制5分钟
            sendWeChat("{} 到货了 {}".format(time.strftime("%H:%M:%S", time.localtime()),text), desp)

        print("{} 无货ing,正在监控".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        sleepTime = random.randint(MONITOR_TIME-100,MONITOR_TIME+100)*0.001
        sleep(sleepTime)

        # 3分钟后重新发送提醒
        countTime += sleepTime
        print(countTime)
        if countTime > COUNT_TIME:
            countTime = 0
            for tmp in hadStockSku:
                searchSkuIds.append(tmp)
            hadStockSku.clear()


if __name__=='__main__':

    if MONITOR_TIME<1500:
        MONITOR_TIME = 1500

    # skuIds = [68418244795, 50619335936, 40857683328, 65585419152]
    skuIds = MONITOR_SKUS
    monitor(skuIds,monitorMode=MONITOR_MODE)