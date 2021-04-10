# 注意：Entry.get()方法必须在Entry pack()时分开两行，否则会报错说没有get()方法

import os
from time import sleep
from random import randint
from PIL import Image
import tkinter as tk
import tkinter.messagebox


def quit():
    global root
    global udisk
    global title
    global content
    global surprise
    global surprise_title
    global surprise_content
    udisk = udisk_et.get()
    title = title_et.get()
    content = content_et.get()
    surprise = surprise_et.get()
    surprise_title = surprise_title_et.get()
    surprise_content = surprise_content_et.get()
    root.destroy()


root = tk.Tk()
root.title('setting')
lb = tk.Label(root, text='使用此程序前请看说明了解具体操作。')
lb.pack()
udisk_lb = tk.Label(root, text='请输入待插入u盘路径：')
udisk_lb.pack()
udisk_et = tk.Entry(root)
udisk_et.pack()
title_lb = tk.Label(root, text='请输入弹窗标题：')
title_lb.pack()
title_et = tk.Entry(root)
title_et.pack()
content_lb = tk.Label(root, text='请请输入弹窗内容：')
content_lb.pack()
content_et = tk.Entry(root)
content_et.pack()
surprise_lb = tk.Label(root, text='请输入惊喜图片名称：')
surprise_lb.pack()
surprise_et = tk.Entry(root)
surprise_et.pack()
surprise_title_lb = tk.Label(root, text='请输入惊喜弹窗标题：')
surprise_title_lb.pack()
surprise_title_et = tk.Entry(root)
surprise_title_et.pack()
surprise_content_lb = tk.Label(root, text='请输入惊喜弹窗内容：')
surprise_content_lb.pack()
surprise_content_et = tk.Entry(root)
surprise_content_et.pack()
bt = tk.Button(root, text='设置', command=quit)
bt.pack()

root.mainloop()


def detect(udisk):
    while True:
        if os.path.exists(udisk):
            break
        else:
            sleep(3)


def box(title, content):
    msg = tk.Tk()

    sw = msg.winfo_screenwidth()
    # 得到屏幕宽度
    sh = msg.winfo_screenheight()
    # 得到屏幕高度
    ww = 100
    wh = 100
    # 窗口宽高为100
    x = (sw - ww) / 2
    y = (sh - wh) / 2
    msg.geometry("%dx%d+%d+%d" % (ww, wh, x, y))

    msg.title(title)
    lb = tk.Label(msg, text=content)
    lb.pack()
    bt = tk.Button(msg, text='确定', command=msg.destroy)
    bt.pack()
    msg.mainloop()


detect(udisk)
dir_list = os.listdir(r"./imgs")
box(title, content)

while True:
    name = dir_list[randint(0, len(dir_list))-1]
    img = Image.open(r'./imgs/'+name)
    img.show()
    if name == surprise:
        box(surprise_title, surprise_content)
        break
    else:
        sleep(1)
