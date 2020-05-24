import re
import threading
import time
import requests
import warnings
warnings.filterwarnings('ignore')

from util import *
import tkinter as tk
from threading import Thread
# from test.test import *



def checkOrder(cookie):
    url = 'https://order.jd.com/center/list.action'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'cookie': cookie
    }

    response = requests.get(url, headers=headers)
    # print('info2:',response.status_code)
    if response.status_code==200:
        # with open("order.txt") as f:
        #     f.write(response.text)
        return True
    return False
    # print(response)

def getqrCodeTicketValidation(ticket):
    url = f'https://passport.jd.com/uc/qrCodeTicketValidation?t={ticket}'
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'referer':'https://passport.jd.com/uc/login?ltype=logout&ReturnUrl=https://order.jd.com/center/list.action'
    }
    response = requests.get(url,headers=headers,verify=False)
    cookieDict = response.cookies.get_dict()
    cookie = ''
    for key,value in cookieDict.items():
        cookie += key + '=' + value + ';'
    # print('info1:',cookie)
    # checkOrder(cookie)
    return cookie

def jdLoginStatus(cookieString, token):
    # 5.轮询二维码状态
    try:
        while True:


            #time.sleep(random.randint(4,7)*0.1)

            time.sleep(1)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
                'referer': 'https://passport.shop.jd.com/nologin/login.action?ReturnUrl=http%3A%2F%2Fshop.jd.com%2F',
                'cookie': cookieString
            }
            checkUrl = f'https://qr.m.jd.com/check?callback=jQuery4643268&appid=133&token={token}&_={round(time.time() * 10000)}'
            checkResponse = requests.get(checkUrl, headers=headers, verify=False)
            checkJson = eval(checkResponse.text[14:-1])

            global loginInfo
            msg = "未扫描"
            if checkJson['code'] == 201:
                msg='二维码未扫描'
                loginInfo.insert('end','二维码未扫描\n')
                print('二维码未扫描')
                pass
            elif checkJson['code'] == 202:
                msg = '手机客户端确认登录'
                loginInfo.insert('end', '手机客户端确认登录\n')
                print('手机客户端确认登录')
                pass
            elif checkJson['code'] == 257:
                msg='无效的二维码'
                loginInfo.insert('end', '无效的二维码\n')
                print('无效的二维码')
                cookie = 2
                loginStatus = 0
                break
            elif checkJson['code'] == 203:
                msg="二维码过期"
                loginInfo.insert('end', '二维码过期\n')
                print('二维码过期')
                cookie = 2
                loginStatus = 0
                break
            elif checkJson['code'] == 200:
                msg="登陆成功"
                loginInfo.insert('end', '登陆成功\n')
                print('登陆成功')
                ticket = checkJson['ticket']

                loginStatus = 1
                # 5.拿着门票去获取登陆后的cookie
                cookie = getqrCodeTicketValidation(ticket)
                # print(cookie)

                res = re.findall(';unick=(.*?);', cookie)
                with open("cookie/cookie_{}.txt".format(res[0]), 'w') as f:
                    f.write(cookie)

                break
            else:
                # 不知道什么状况
                msg='未知状况'
                loginInfo.insert('end', '未知状况\n')
                cookie = 2
                loginStatus = 0
                break


        print("cookie:")

        print(cookie)

        loginInfo.insert('end','窗口3s后关闭')
        time.sleep(3)
        closeWindow()

        return {'status': 1, 'loginStatus': loginStatus,'msg':msg, 'cookie': cookie}

    except:
        return {'status': 0}

def getjdQrCode():
    try:

        # 1.获取二维码
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
            'referer': 'https://passport.jd.com/new/login.aspx?ReturnUrl=https%3A%2F%2Fwww.jd.com%2F'
        }

        qrCodeUrl = f'https://qr.m.jd.com/show?appid=133&size=147&t={round(time.time() * 10000)}'
        qrHtml = requests.get(qrCodeUrl, headers=headers)
        cookies = qrHtml.cookies.get_dict()
        token = cookies['wlfstk_smdl']
        cookieString = ''
        for key, value in cookies.items():
            cookieString = cookieString + str(key) + "=" + str(value) + ";"
        cookieString = r'%s' % (cookieString)

        # 2.下载二维码到本地
        fileName='qrCode.jpg'
        with open(fileName, 'wb')as f:
            f.write(qrHtml.content)
        # with open(fileName, 'rb') as f:
        #     base64_data = str(base64.b64encode(f.read()))
        # base64Data = re.findall("b'(.*)'", base64_data)[0]
        # base64Data = r'%s' % (base64Data)

        # sleep(1)
        # global window

        # 3.异步轮询二维码状态
        # threading.Thread(target=jdLoginStatus, args=(cookieString, token)).start()
        # return jdLoginStatus(cookieString,token)
        # imgCode = base64Data
        # return {'status': 1, 'imgCode': imgCode, 'cookieString': cookieString, 'token': token}

        return {'status':1,'cookieString':cookieString,'token':token}

    except:
        return {'status': 0}


class GetCookiesThread(threading.Thread):
    def __init__(self,cookieString,token):
        Thread.__init__(self)
        self.cookieString=cookieString
        self.token=token

    def run(self):
        self.result = jdLoginStatus(self.cookieString,self.token)

    def getResult(self):
        return self.result



def getWindow():
    window = tk.Tk()
    window.title("扫码登陆")
    window.geometry('200x400')
    window.resizable(False, False)
    return window


def closeWindow():
    global  window
    window.destroy()

def loginOne():
    window = getWindow()

    # 生成qr图片
    qrRes = getjdQrCode()
    if qrRes['status'] == 1:
        fileName = 'qrCode.jpg'
        canvas = tk.Canvas(window, bg='white', height=200, width=200)
        image_file = tk.PhotoImage(file=fileName)
        image = canvas.create_image(25, 25, anchor='nw', image=image_file)
        canvas.pack()

        loginInfo = tk.Text(window, height=100)
        loginInfo.pack()
        # text.insert('end',"test")

        thd = threading.Thread(target=jdLoginStatus, args=(qrRes['cookieString'], qrRes['token'])).start()
        # thd = GetCookiesThread(qrRes['cookieString'],qrRes['token']).start()

        window.mainloop()

    else:
        print("获取登录二维码异常")


if __name__=='__main__':

    # while True:
    #     print("1:登录 2:退出")
    #     print("请输入：")
    #     s = input()
    #     if '2'==s:
    #         break
    #     if '1'==s:
    #         loginOne()
    #     else:
    #         print("输入错误，重新输入：")


    window = getWindow()

    # 生成qr图片
    qrRes = getjdQrCode()
    if qrRes['status'] == 1:
        fileName = 'qrCode.jpg'
        canvas = tk.Canvas(window, bg='white', height=200, width=200)
        image_file = tk.PhotoImage(file=fileName)
        image = canvas.create_image(25, 25, anchor='nw', image=image_file)
        canvas.pack()

        loginInfo = tk.Text(window, height=100)
        loginInfo.pack()
        # text.insert('end',"test")

        thd = threading.Thread(target=jdLoginStatus, args=(qrRes['cookieString'], qrRes['token'])).start()
        # thd = GetCookiesThread(qrRes['cookieString'],qrRes['token']).start()

        window.mainloop()

    else:
        print("获取登录二维码异常")


    print("结束登录...")





