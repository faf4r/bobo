import os
import time
import random
from PIL import Image
import tkinter as tk
import tkinter.messagebox
'''
请确保该文件与图片文件夹在同一目录内
'''

def detect():
    while True:
        if os.path.exists('F://'):
            break
        else:
            time.sleep(3)
detect()

dir_name = '唯美img'
dir_list = os.listdir(r"./"+dir_name)
tk.messagebox.showwarning('波波愚人节快乐', '波波愚人节快乐！')
while True:
    name = dir_list[random.randint(0,len(dir_list))]
    img=Image.open(r'./唯美img/'+name)
    img.show()
    if name == '物理.png':
        tk.messagebox.showwarning('运气爆棚', '波波太强了，千分之一的概率都中了，打断循环，让我们开始快乐的物理课吧！')
        break
    else:
        time.sleep(1)



