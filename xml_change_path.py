import xml.etree.ElementTree as ET
import os
import sys

def traverseXml(element):
    #print (len(element))
    if len(element)>0:
        for child in element:
            print (child.tag, "----", child.attrib)
            traverseXml(child)
    #else:
        #print (element.tag, "----", element.attrib)
        

if __name__ == "__main__":
    xmlFilePath = os.path.abspath("blacktea.xml")
    print(xmlFilePath)
    try:
        tree = ET.parse(xmlFilePath)
        print ("tree type:", type(tree))
    
        # 獲得根節點
        root = tree.getroot()
    except Exception as e:  #捕獲除與進程退出sys.exit()相關之外的所有異常
        print ("parse test.xml fail!")
        sys.exit()
    print ("root type:", type(root))    
    print (root.tag, "----", root.attrib)
    
    #遍歷root的下一層
    for child in root:
        print ("遍歷root的下一層", child.tag, "----", child.attrib)


    data = root.find('path')
    print(data.text)
    data.text = "C:\\Users\\王利倫\\Desktop\\opencv\\save\\blacktea.jpg"
    print(data.text)
    #root.set(data,'path')
    tree.write('blacktea.xml',xml_declaration=True)
    #root.set('path',data)
    

"""
    #使用下標訪問
    print (root[0].text)
    print (root[1][1][0].text)

    print (20 * "*")
    #遍歷xml文檔
    traverseXml(root)
    print (20 * "*")

    #根據標籤名查找root下的所有標籤
    captionList = root.findall("item")  #在當前指定目錄下遍歷
    print (len(captionList))
    for caption in captionList:
        print (caption.tag, "----", caption.attrib, "----", caption.text)

    #修改xml文檔，將passwd修改為999999
    login = root.find("login")
    passwdValue = login.get("passwd")
    print ("not modify passwd:", passwdValue)
    login.set("passwd", "999999")   #修改，若修改text則表示為login.text
    print ("modify passwd:", login.get("passwd"))
"""
