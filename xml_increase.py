import xml.etree.ElementTree as ET
import os
import sys

if __name__ == "__main__":
    xmlFilePath = os.path.abspath("./photo/data/milktea.xml")
    print(xmlFilePath)
    try:
        tree = ET.parse(xmlFilePath)
        print ("tree type:", type(tree))
    
        # 獲得根節點
        root = tree.getroot()
    except Exception as e:  #捕獲除與進程退出sys.exit()相關之外的所有異常
        print ("parse test.xml fail!")
        sys.exit()

    for i in range(100):
        tree.write('./VOCdevkit/VOC2007/Annotations/milktea_'+str(i)+'.xml',encoding='UTF-8')


