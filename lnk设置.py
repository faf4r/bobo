# https://blog.csdn.net/weixin_43903378/article/details/94392277
import os
import pythoncom
from win32com.shell import shell
from win32com.shell import shellcon


def set_shortcut():  # 如无需特别设置图标，则可去掉iconname参数
    try:
        filename = r"D:\AppServ\timer\win_cron_zq\timer.exe"  # 要创建快捷方式的文件的完整路径
        iconname = ""
        lnkname = r"C:\Users\pc1\Desktop" + r"\timer.exe.lnk"  # 将要在此路径创建快捷方式

        shortcut = pythoncom.CoCreateInstance(
            shell.CLSID_ShellLink, None,
            pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)
        shortcut.SetPath(filename)

        shortcut.SetWorkingDirectory(r"D:\AppServ\timer\win_cron_zq") # 设置快捷方式的起始位置, 不然会出现找不到辅助文件的情况
        shortcut.SetIconLocation(iconname, 0)  # 可有可无，没有就默认使用文件本身的图标
        if os.path.splitext(lnkname)[-1] != '.lnk':
            lnkname += ".lnk"
        shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(lnkname, 0)

        return True
    except Exception as e:
        print(e.args)
        return False
