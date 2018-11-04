import cv2
import numpy as np
from PIL import Image
import os

path = "./photo/myobject"

filelist = os.listdir(path)
total_num = len(filelist)

#i = 1
n = 6
for i in range(1,total_num + 1):
    n = 6 - len(str(i))
    filepath = "./photo/myobject/"+str(0)*n + str(i)+".jpg"
    imgsize = Image.open(filepath)#開啟圖片
    img = cv2.imread(filepath)
    img = cv2.resize(img, (imgsize.size[1]//4,imgsize.size[0]//4), interpolation=cv2.INTER_CUBIC)
    #參考https://blog.csdn.net/qq_40979622/article/details/80709924
    #將“/”改为“//”运算
    cv2.imwrite(filepath,img)


