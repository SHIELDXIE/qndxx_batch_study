#首次运行安装必要库
import os

#需要安装的库
libs = ["requests"]

#循环遍历安装
for lib in libs:
    os.system("pip install " + lib)
