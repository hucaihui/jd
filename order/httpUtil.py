import requests
import json
from config import *


def getPage(url,headers=None):
    try :
        if headers is None:
            resp= requests.get(url)
        else:
            resp = requests.get(url,headers=headers)
        if resp.status_code==200:
            return resp.text
        return None
    except ConnectionError:
        print("err:cannot to connect to",url)
        return None



def postJsonData(url,data):
    if type(data) is not str:
        data =json.dumps(data)    #dict --> str
    # print(type(data))

    headers = {
        'content-type': "application/json"
    }
    try:
        resp = requests.post(url, headers=headers, data=data)
        if resp.status_code==200:
            return True
    except Exception as e:
        print(e)
        print("请求{}失败".format(url))

    return False

def getJsonData(url,header=None):
    try:
        if header is None:
            resp = requests.get(url)
        else:
            resp = requests.get(url,header)
        if resp.status_code==200:
            j =json.loads(resp.text)
            return j
        return None
    except Exception as e:
        print(e)
        print("请求{}失败".format(url))
    return None

if __name__=='__main__':
    data = {
        "sku": "fff",
        "articleNo": "aaa",
        "color": "aaa ",
        "size": " aa"
    }

    url = PRE_URL + "/goods/insert"


    postJsonData(url,data)
