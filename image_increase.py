import cv2

path = './photo/data/milktea.jpg'

for i in range(100):
    img = cv2.imread(path)
    cv2.imwrite('./save/milktea_'+str(i)+'.jpg',img)

