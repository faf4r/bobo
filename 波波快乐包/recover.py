import os, re

name_listdir = os.listdir('F://')
for name in name_list:
    if re.search('#.*?\.lnk', name) is not None:
        os.remove('F://'+name)
    else:
        pass
    print('已删除：', name)

print('已全部删除')
