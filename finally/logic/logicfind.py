"""
    Description:设置内容查找的界面功能并绑定控件
    Autor:
    Date: 2020-06-13 18:02:04
    LastEditTime: 2020-11-14 19:58:33
    LastEditors: VanderWaals
"""
import re
import sys
import os
import os.path
from win32com import client as wc
# import docx
from PyQt5.QtWidgets import *
import jieba
import wordcloud
from ui import uifind
class myfind(uifind.Ui_MainWindow):
    def __init__(self):
        """
            description: 初始化并绑定控件
            return:
        """
        super(myfind,self).__init__()
        self.setupUi(self)
        self.pushButton1.clicked.connect(self.run)
        self.pushButton2.clicked.connect(self.draw)
        self.actiondakai.triggered.connect(self.select)
    def printf(self,text):
        """
            description: 差异化输出
                        1. 匹配字段
            return:
        """
        self.textBrowser.append("<font color='red'>"+"\"\""+"</font>"+text.replace(self.key,"<font color='red'>"+self.key+"</font>")+"<font color='red'>"+"\"\""+"</font>")
    def tips(self,form):
        """
            description: 提示
            return:
        """
        if form==0:
            QMessageBox.warning(
                self,
                "错误",
                "不支持该类型文件",
                QMessageBox.Ok
                                )
    def select(self):
        """
            description: 选择文件
            return:
        """
        fm=QFileDialog.getOpenFileName( self,"打开",'.',"word2016(*.docx);;word2007(*.doc);;excle(*.xlsx);;文本文件(*.txt)")
        if fm[0]:
            self.lineEdit1.setText(fm[0])
    def run(self):
        """
            description: 处理变量并调起打开文件函数
            return:
        """
        self.path = self.lineEdit1.text()                       #获取文件路径
        self.key = self.lineEdit2.text()                        #获取关键字
        self.pattern = re.compile(r"^.*?(%s).*?$" % self.key)   #确定正则匹配模式
        self.kinds={                                            #支持的文件类型
                "doc":1,
                "docx":1,
                "xls":2,
                "xlsx":2,
                "txt":3,
                }
        self.ext=os.path.split(self.path)[-1].split('.')[-1]    #解析出扩展名
        self.openfile()                                         #调用函数
    def deal(self,*ls):
        """
            description: 供输出文件统一输出
            return:
        """
        if ls[0]==1:
            self.textBrowser.clear()
            for p in ls[-1].paragraphs:                         #对于word文件，按段落打印
                if re.match(self.pattern, str(p.text)):
                    self.printf(str(p.text))
        if ls[0]==2:
            self.textBrowser.clear()
            for sheet in ls[2]:
                line = ls[1].sheet_by_name(sheet)
                for i in range(0,line.nrows):
                    for j in range(0,line.ncols):
                        if re.match(self.pattern, str(line.cell_value(i,j))):
                            self.printf(line.cell_value(i,j))   #excle按单元格打印
    def openfile(self,mode=0):
        """
            description: 打开文件，具有两种模式
                        1.供 deal()进行处理
                        2.供 draw()进行处理
            return:
        """
        filekind=self.kinds.get(self.ext,0)
        if filekind == 0:
            self.tips(filekind)
            return
        elif filekind==1:
            if filekind=='doc':
                word = wc.Dispatch("Word.Application")          #打开word应用程序
                doc = word.Documents.Open(self.path)            #打开word文件
                doc.SaveAs("{}x".format(self.path), 12)         #另存为后缀为".docx"的文件，其中参数12指docx文件
                doc.Close()                                     #关闭原来word文件
                word.Quit()
            doc = docx.Document(self.path)
            if mode==0: self.deal(filekind,doc)                 #模式0
            return (filekind,doc)
        elif filekind==2:
            xls_workbook=xlrd.open_workbook(self.path)          #打开excle文件
            xls_worksheets=xls_workbook.sheet_names()
            if mode==0: self.deal(filekind,xls_workbook,xls_worksheets)
            return (filekind,xls_workbook,xls_worksheets)
        elif filekind==3:
            if mode==0:
                count=0
                with open(self.path,'r',encoding='utf8') as f:  #文本文件
                    for index,line in enumerate(f):
                        count+=1
                self.textBrowser.clear()
                with open(self.path,'r',encoding='utf8') as f:
                    for i in range(0,count):
                        text=f.readline()
                        if re.match(self.pattern, str(text)):
                            self.printf(text)
                return (filekind)
    def out(self,text):
        """
            description: 输出词云图片
            return:
        """
        self.textBrowser.append("<font color='red'>"+"正在生成词云，请稍侯......"+"</font>")
        temp=jieba.lcut(text)
        text="".join(temp)
        alpha=wordcloud.WordCloud(height=1080,width=1920,font_path='msyh.ttc')
        alpha.generate(text)
        alpha.to_file(self.name)
        self.textBrowser.append("<font color='red'>"+"词云已生成！"+"</font>")
    def draw(self):
        """
            description: 为不同类型文件统一调用out()
            return:
        """
        self.path = self.lineEdit1.text()
        self.name=self.lineEdit2.text()
        self.kinds={
                "doc":1,
                "docx":1,
                "xls":2,
                "xlsx":2,
                "txt":3,
                }
        self.ext=os.path.split(self.path)[-1].split('.')[-1]
        ls=list(self.openfile(mode=1))
        if ls[0]==1:
            text=""
            for p in ls[-1].paragraphs:
                text+=p.text
        if ls[0]==2:
            text=""
            for sheet in ls[2]:
                line = ls[1].sheet_by_name(sheet)
                for i in range(0,line.nrows):
                    for j in range(0,line.ncols):
                        text+=line.cell_value(i,j)
        self.out(text)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = myfind()
    ui.show()
    sys.exit(app.exec_())