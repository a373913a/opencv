import cv2
import numpy as np
from PIL import Image
import os
from numba import vectorize
import time

@vectorize('float64(float64,float64)',target='cuda')
def grabcut_gpu(w,h):
    filepath = "./photo/myobject/000001.jpg"
    img = cv2.imread(filepath)
    mask = np.zeros(img.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    rect = (50,20,w,h)
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)##
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    return img*mask2[:,:,np.newaxis]
    

imgsize = Image.open(filepath)#開啟圖片

output = grabcut_gpu(imgsize.size[0],imgsize.size[1])

cv2.imwrite('./save/test.jpg',output)
