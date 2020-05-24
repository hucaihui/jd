import os
import  requests
import tkinter as tk
import pandas as pd

def readCookie(fileName):
    if not os.path.isfile(fileName):
        print(fileName + ' file not exist')


    with open(fileName) as f:
        cookie = f.read()

    return cookie

def getCookieDict(dir):
    cookieDict= {}

    for file in os.listdir(dir):
        fileName = dir + "/"
        try:
            username = str(file).split('_')[1].split('.')[0]
            fileName += file
            # print(fileName)
            cookie = readCookie(fileName)
            cookieDict[username] = cookie

        except Exception as e:
            print(e)
            print("file [{}] name is not correct".format(file))
            continue


    return cookieDict


def isNumber(s):
    try:

        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

# def isSize(s):
#     sizeList = ['s','m','l','xl','xxl','xxl']
#     if s.toLow

class FilePtr():
    def __init__(self,fileName):
        self.fileName=fileName
        self.df  = None
        self.flag = False

    def put(self,content):
        self.flag = True
        if self.df is None:
            self.df = pd.DataFrame(content,index=[0])
        else:
            tmp = pd.DataFrame(content,index=[1])
            self.df = self.df.append(tmp,ignore_index=True)
        # print(self.df)


    def close(self):
        if self.flag:
            self.df.to_excel(self.fileName)


filePtrDict = {}
def getFilePtr(fileName):
    if fileName not in filePtrDict:
        filePtrDict[fileName] = FilePtr(fileName)

    filePtr = filePtrDict[fileName]
    return filePtr

# 保存文件
def saveToFile(fileName):
    try:
        filePtrDict[fileName].close()
    except Exception as e:
        print("error:save file:",fileName)
        print(e)



def getWindow():
    window = tk.Tk()
    window.title("扫码登陆")
    window.geometry('300x200')
    # window.resizable(False, False)
    return window

def closeWindow():
    global  window
    window.destroy()

# class OrderInfo():
#     def __init__(self):
#         self.fileDict = {}
#
#
#     def getFilePtr(self,name):

def testCookieDict():
    cookieDict = getCookieDict("cookie")
    print(cookieDict)

def testFilePtrClass():
    filePtr = FilePtr("test.xlsx")
    filePtr.put({"a":1,"b":2,"c":3})
    filePtr.put({"a":11,"b":22,"c":33})
    filePtr.close()

if __name__=="__main__":
    # testCookieDict()

    testFilePtrClass()

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'referer': 'https://order.jd.com/center/list.action',

    }