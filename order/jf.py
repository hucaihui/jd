

import requests


if __name__=='__main__':
    startUrl = "https://item.jd.com/65585419154.html"

    url = 'https://qwd.jd.com/cps/zl'
    cookie = 'client_type=android;app_id=161;login_mode=2;jxjpin=a13218343010;tgt=AAJd9mHUAEDhOPEdYretO6pvIbiRA0k5qa4wxW54YXoWTxhftHC77mIvuingsM9tqciD3T0PHSZYdVPTSTAx7zCwD-Kd-z0V;qwd_chn=99;qwd_schn=1;jfShareSource=1_2_1'
    headers ={
        'host':'qwd.jd.com',
        'cookie':cookie,
        'user-agent':'jxj/3.7.4',
        'connection':'keep-alive',

    }

    params = {
        'content':startUrl,
        'shareSource':'1_2_1',
    }

    resp = requests.get(url,headers=headers,params=params)
    print(resp.text)