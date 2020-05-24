
from datetime import datetime


# 公共配置

PRE_URL='http://hucaihui.cn:9200'

COMMON_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
}



########   订单提取 getOrder.bat
D = 1                                  #  =1:近三个月的订单     =2:今年内订单
START_TIME=str(datetime(2020,4,1))     # 开始时间
# END_TIME = datetime.now()            # 结束时间1  当前时间
END_TIME = str(datetime(2020,5,18))    # 结束时间2  自定义
MIN_MONEY=200                          # 最小金额



########## 地区id
AREA = '19_1659_37259_37283'

########## 鞋码范围
MIN_SIZE = 35
MAX_SIZE = 45

########## 搜索 stock.bat
SEARCH_MODE = 2        # 搜索模式   1：仅扫描当前sku下的所有尺码   2：当描当前sku下的所有 规格 的尺码
SEARCH_SKUS = [57528850652,68418244795,50619335936,40857683328,65585419152,59149202098]


########## 监控  monitor.bat
MONITOR_TIME = 3000    # 单位: ms   最少2000ms
COUNT_TIME = 600       # 单位：s    已到货商品 **s后会重新提醒
MONITOR_MODE = 2       # 1：监控指定sku   2：监控指定sku的所有尺码
MONITOR_SKUS = [59149202098,57528850651]

# 消息提醒        SCKEY如何获取：http://sc.ftqq.com/?c=code
SCKEY = "SCU97212T29cd9bee9f99bab650070de5ee7b3cbb5eb6c351e0a7b"


