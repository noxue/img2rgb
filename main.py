from tkinter import E
from PIL import Image
from pip import main
import numpy as np

import sys



def file2array(path):
    # 获取文件名
    if '\\' in path:
        filename = path.split('\\')[-1]
    else:
        filename = path.split('/')[-1]
    tmp = filename.split('\\')[-1]
    # 去除后缀
    name = tmp.split('.')[0]
    # print(name)

    image=Image.open(path)
    out = image.convert("RGB")
    img=np.array(out)

    # print(out.size)
    # print("宽高：",img.shape)#高 宽 三原色分为三个二维矩阵

    # 缩放图片
    out.thumbnail((50,50))
    img=np.array(out)



    # 缩小图片
    img_small=img
    print("//" + str(name))

    # 转c语言数组初始化
    img_small_c=img_small.tolist()
    # img_small_c=img_small.tolist()

    print(("int img_%s[%d][%d][%d] = " % (name,img_small.shape[0],img_small.shape[1],img_small.shape[2]))+str(img_small_c).replace("[","{").replace("]","}")+";\n\n")

if __name__ == '__main__':
    import os
    if len(sys.argv) < 2:
        print("Usage: python main.py image_file [image_file...]")
        sys.exit(1)

    for path in sys.argv[1:]:
        file2array(path)
