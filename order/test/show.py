import re
import threading
import tkinter as tk
from threading import Thread
from time import sleep

def getWindow():
    window = tk.Tk()
    window.title("扫码登陆")
    window.geometry('300x200')
    # window.resizable(False, False)
    return window

def closeWindow():
    global  window
    window.destroy()

if __name__=='__main__':
    window=getWindow()
    fileName= '../qrCode.jpg'


    # canvas = tk.Canvas(window, bg='white', height=200, width=200)
    # image_file=tk.PhotoImage(file=fileName)
    # image = canvas.create_image(25, 25, anchor='nw', image=image_file)
    #
    # canvas.pack()
    # window.mainloop()


    str = 'TrackID=1QsEBUkqTMwMbAsZ3lRLsUzDk4dTwilCM3zdhlsHhYfrEiCKWzbcPO9O7OtQNMMe5oa8yYcox0GXEoegVRc3HOEIUAvz64DfOcqsIoS0Sc5Q;_pst=a13218343010;_tp=b1T8WFuIvS9LmVQfwB1u3A%3D%3D;ceshi3.com=201;logining=1;pin=a13218343010;pinId=UpGv8tRsfjHGQzxH7Tl0fA;thor=99BA847818BB06A0898AFF57B36E2DAD1F217B7F33687724CAA365C3B3B2CE732E33F7EF1F77AAD2CDC6E9816D3E8232AD626E0FB00D5E4B34DF4608139A7633B6BD1BD1CF649E7505CED4865E131681F71ED56C570889A464D0373FA1986C8F416D03AEEE7F2B7D96B402FBE976304EFF58109433CE3590655B7A82DD3B39ACFE8B4A33A514AF7A31185524342291D5;unick=a13218343010;DeviceSeq=aa8704dc2b044845a5766f7b749f4417;'

    res = re.findall(';_pst=(.*?);',str)
    print(res)