import cv2

video = "test2.mp4"
cap = cv2.VideoCapture(video)

# 設定擷取影像的尺寸大小
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

# 使用 XVID 編碼
fourcc          = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') 
video_fps       = cap.get(cv2.CAP_PROP_FPS)
video_size      = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                        int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# 建立 VideoWriter 物件，輸出影片至 output.avi

out = cv2.VideoWriter("output.mp4", fourcc, video_fps, video_size)

while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    # 寫入影格
    out.write(frame)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break

# 釋放所有資源
cap.release()
out.release()
cv2.destroyAllWindows()
