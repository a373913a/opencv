from yolo import YOLO
from tkinter import *
from tkinter.ttk import *
import threading, time

win = Tk()
win.title("圖片爬蟲")#標題
win.geometry("300x100")#設定視窗大小

img_name = Label(win,text="圖片")
img_entry = Entry(win)

"""
def detect_img(yolo):

    img = str(img_entry.get())
    print(img)
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        
    else:
        r_image = yolo.detect_image(image)
        r_image.show()
    yolo.close_session()
"""

def detect_img(yolo):
    while True:
        img = input('Input image filename:')
        print(img)
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.show()
    yolo.close_session()
    
class MyClass (threading.Thread): # 繼承 Thread 類別
    
    def run(self): # 覆載 (Override) Thread 類別的方法(函數)
        detect_img(YOLO())
        #print("OK")



def Yolo_action():
    test = MyClass()
    test.start()

    
compute = Button(win,text="開始",command=Yolo_action)
#=================================排版=================================
img_name.grid(row = 0,column = 0)
img_entry.grid(row = 0,column = 1)
compute.grid(row = 0,column = 2)


win.mainloop()#視窗產生
