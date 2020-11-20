"""
    Description:
    Autor: VanderWaals
    Date: 2020-05-25 16:59:41
    LastEditTime: 2020-05-25 16:59:42
    LastEditors: VanderWaals
"""
from re import match
import docx
while True:
    print("\t\t\t************文件选择************")
    path=input("\t\t\t请输入文件路径(提示：输入‘退出’关闭程序)：")
    if path=='退出':
        break
    file=docx.Document(path)
    while True:
        print("\t\t\t************关键字选择************")
        key=input("\t\t\t请输入关键字(提示：输入 ‘退出’ 返回上一级)：")
        if key=="退出":
            break
        flag=0
        for p in file.paragraphs:
            if match("^.*?"+key+".*?$",str(p.text)):
                print("\n"+p.text+"\n")
                flag=1
        if not flag:
            print("\t\t\t文件中不存在关键字："+key)