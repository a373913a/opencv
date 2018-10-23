import cv2
import numpy as np
from scipy import ndimage
from PIL import Image
from matplotlib import pyplot as plt

filepath = "./photo/myobject/000001.jpg"

imgsize = Image.open(filepath)#開啟圖片


img = cv2.imread(filepath)

mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (100,40,imgsize.size[0],imgsize.size[1])
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

cv2.imwrite('./save/000001.jpg',img)
cv2.imshow('show',img)
cv2.waitKey()
cv2.destroyAllWindows()
#plt.imshow(img),plt.colorbar(),plt.show()


'''
img = cv2.imread('./photo/myobject/P_20181020_214925.jpg',0)
cv2.imwrite('./save/P_20181020_214925.jpg',img)
cv2.imshow('show',img)
cv2.waitKey()
cv2.destroyAllWindows()
'''


