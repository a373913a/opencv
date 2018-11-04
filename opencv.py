import cv2
import numpy as np
from PIL import Image
import os
import time

path = "./photo/myobject"

filelist = os.listdir(path)
total_num = len(filelist)



    
n = 6
for i in range(1,total_num):
    n = 6 - len(str(i))
    filepath = "./photo/myobject/"+str(0)*n + str(i)+".jpg"
    imgsize = Image.open(filepath)#開啟圖片
    print('開啟檔案：' + filepath)
    img = cv2.imread(filepath)
    
    mask = np.zeros(img.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    print(type(imgsize.size[0]))
    rect = (50,20,imgsize.size[0],imgsize.size[1])
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)##
    
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    
    img = img*mask2[:,:,np.newaxis]
    
    cv2.imwrite('./save/'+str(0)*n + str(i)+'.jpg',img)
    
    print("mask2花費時間：%s" %(end-start))
    



    """
n = 6
for i in range(1,total_num):
    start = time.time()
    n = 6 - len(str(i))
    filepath = "./photo/myobject/"+str(0)*n + str(i)+".jpg"
    imgsize = Image.open(filepath)#開啟圖片
    print('開啟檔案：' + filepath)
    img = cv2.imread(filepath)
    mask = np.zeros(img.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    rect = (50,20,imgsize.size[0],imgsize.size[1])
    cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]
    cv2.imwrite('./save/'+str(0)*n + str(i)+'.jpg',img)
    end = time.time()
    print("花費時間：%s" %(start-end))


    for a in range(1,101):
        for b in range(1,101):
            print('round %s_%s_%s' % (str(i),str(a),str(b)))
            img = cv2.imread(filepath)
            mask = np.zeros(img.shape[:2],np.uint8)
            bgdModel = np.zeros((1,65),np.float64)
            fgdModel = np.zeros((1,65),np.float64)
            rect = (a,b,imgsize.size[0],imgsize.size[1])
            cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
            mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
            img = img*mask2[:,:,np.newaxis]
            print('輸出檔案：%s_%s_%s.jpg' %(str(0)*n + str(i),str(a),str(b)))
            cv2.imwrite('./save/%s_%s_%s.jpg' %(str(0)*n + str(i),str(a),str(b)),img)
            
    """
