import os, time, re, shutil, random
def detect():
    while True:
        if os.path.exists('F://'):
            break
        else:
            time.sleep(3)


#detect()
lnks = os.listdir('./lnks')
# print(lnks)
try:
    shutil.copy2(lnks[random.randint(0,len(lnks))], 'F://')
except Exception as e:
    print(e)

