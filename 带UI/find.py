"""
    Description:
    Autor: VanderWaals
    Date: 2020-05-25 17:47:47
    LastEditTime: 2020-05-26 17:52:21
    LastEditors: VanderWaals
"""
import sys
import re
import os
import os.path
from win32com import client as wc
import cgitb
from functools import partial
import docx
from PyQt5.QtWidgets import *
from PIL import Image
import xlrd, xlwt
import UI

def printf(text):
    for i in str(text):
        ui.textBrowser.append("<font color='red'>"+i+"</font>") if i in key else ui.textBrowser.append("<font color='black'>"+i+"</font>")
        ui.textBrowser.deleteLater()
    print("\n")

def openfile(ui,path,ext):
    global kinds
    filekind=kinds.get(ext,0)
    if filekind == 0:
        ui.tips(filekind)
        return
    elif filekind==1:
        if filekind=='doc':
            word = wc.Dispatch("Word.Application") # 打开word应用程序
            doc = word.Documents.Open(path) #打开word文件
            doc.SaveAs("{}x".format(path), 12)#另存为后缀为".docx"的文件，其中参数12指docx文件
            doc.Close() #关闭原来word文件
            word.Quit()
        doc = docx.Document(path)
        ui.textBrowser.clear()
        for p in doc.paragraphs:
            if re.match(pattern, str(p.text)):
                printf(p.text)

    elif filekind==2:
        xls_workbook=xlrd.open_workbook(path)
        xls_worksheets=xls_workbook.sheet_names()
        ui.textBrowser.clear()
        for sheet in xls_worksheets:
            line = xls_workbook.sheet_by_name(sheet)
            for i in range(0,line.nrows):
                for j in range(0,line.ncols):
                    if re.match(pattern, str(line.cell_value(i,j))):
                        printf(line.cell_value(i,j))
    elif filekind==3:
        count=0
        with open(path,'r',encoding='utf8') as f:
            for index,line in enumerate(f):
                count+=1
        with open(path,'r',encoding='utf8') as f:
            for i in range(0,count):
                text=f.readline()
                if re.match(pattern, str(text)):
                    printf(text)



def deal(ui):
    global path
    path = ui.lineEdit.text()
    global key
    key  = ui.lineEdit_2.text()
    global pattern
    pattern = re.compile(r"^.*?(%s).*?$" % key)
    if path == '' or key == '':
        return
    ext=os.path.split(path)[-1].split('.')[-1]
    openfile(ui,path,ext)


if __name__ == '__main__':
    cgitb.enable( format = 'text')
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = UI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(partial(deal, ui))
    path = ""
    key = ""
    pattern = ""
    kinds={
            "doc":1,
            "docx":1,
            "xls":2,
            "xlsx":2,
            "txt":3,
            }
    sys.exit(app.exec_())
