import numpy as np
import cv2
import os
from PIL import Image
path = "./photo/myobject"

filelist = os.listdir(path)
total_num = len(filelist)

n = 6
for i in range(1,total_num):
    n = 6 - len(str(i))
    filepath = "./photo/myobject/"+str(0)*n + str(i)+".jpg"
    imgsize = Image.open(filepath)#開啟圖片
    print('開啟檔案：' + filepath)
    imgo = cv2.imread(filepath)
    height, width = imgo.shape[:2]
    mask = np.zeros(imgo.shape[:2],np.uint8)
    bgdModel = np.zeros((1,65),np.float64)
    fgdModel = np.zeros((1,65),np.float64)
    rect = (50,20,width-30,height-30)
    cv2.grabCut(imgo,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
    mask = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img1 = imgo*mask[:,:,np.newaxis]
    background = imgo - img1
    background[np.where((background > [0,0,0]).all(axis = 2))] =[0,0,255]
    final = background + img1
    cv2.imwrite('./save/'+str(0)*n + str(i)+'.jpg',final)
    
"""
#Load the Image
imgo = cv2.imread(‘input.jpg’)
height, width = imgo.shape[:2]

#Create a mask holder
mask = np.zeros(imgo.shape[:2],np.uint8)

#Grab Cut the object
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

#Hard Coding the Rect… The object must lie within this rect.
rect = (10,10,width-30,height-30)
cv2.grabCut(imgo,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask = np.where((mask==2)|(mask==0),0,1).astype(‘uint8’)
img1 = imgo*mask[:,:,np.newaxis]

#Get the background
background = imgo – img1

#Change all pixels in the background that are not black to white
background[np.where((background > [0,0,0]).all(axis = 2))] =[255,255,255]

#Add the background and the image
final = background + img1
"""
