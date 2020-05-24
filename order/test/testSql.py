

import requests
import json
from httpUtil import *

if __name__=='__main__':

    # url = 'http://localhost:8080/goods/selectAll'
    # url = 'http://localhost:8080/goods/selectOne?id=41507444717'
    # resp = requests.get(url)
    #
    # if resp.status_code==200:
    #
    #     print(resp.text)
    #     j = json.loads(resp.text)
    #     print(j['success'],j['obj']['sku'])



    print(postJsonData(PRE_URL+"/shop/insert",{"shopNo":100,"shopName":"aaa"}))