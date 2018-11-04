import cv2
 
capture = cv2.VideoCapture('test2.mp4')
 
#cv2.VideoCapture.get(CV_CAP_PROP_FORMAT)
fps = capture.get(cv2.CAP_PROP_FPS)
print ('fps is ' + str(fps))
 
codec = int(capture.get(cv2.CAP_PROP_FOURCC))
print ('codec is %x'%(codec))
print ('codec is ' + chr(codec&0xFF) + chr((codec>>8)&0xFF) + chr((codec>>16)&0xFF) + chr((codec>>24)&0xFF))
