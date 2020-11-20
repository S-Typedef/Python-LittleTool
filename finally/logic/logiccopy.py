"""
    Description:设置批量复制的界面功能并绑定控件
    Autor:
    Date: 2020-06-13 15:00:31
    LastEditTime: 2020-06-13 15:00:31
    LastEditors:
"""
import re
import os
import os.path
import time
import shutil
import sys
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from ui import uicopy
class mycopyui(uicopy.Ui_MainWindow):
    def __init__(self):
        """
            description: 初始化界面并绑定
            return:
        """
        super(mycopyui,self).__init__()
        self.setupUi(self)
        self.pushButton2.clicked.connect(self.select_dir1)
        self.pushButton3.clicked.connect(self.select_dir2)
        self.pushButton1.clicked.connect(self.run)
    def select_dir1(self):
        """
            description: 绑定打开源文件目录
            return:
        """
        self.fm=QtWidgets.QFileDialog.getExistingDirectory(self,"打开",'.')
        self.lineEdit.setText(self.fm)
    def select_dir2(self):
        """
            description: 绑定打开目标目录
            return:
        """
        self.fm=QtWidgets.QFileDialog.getExistingDirectory(self,"打开",'.')
        self.lineEdit2.setText(self.fm)
    def ecopy(self,path,tar,tol_ext):
        """
            description: 递归式执行复制操作
            return:
        """
        if os.path.isfile(path):
            file_path = os.path.split(path)  # 分割出目录与文件
            # 分割出文件与文件扩展名  lists[0]:name,lists[1]:ext
            lists = file_path[1].split('.')
            lists_2 = file_path[0].split("\\")  # lists_2[-2]:父目录名
            file_ext = lists[-1]  # 取出后缀名(列表切片操作)
            if file_ext in tol_ext:
                newfile = tar+"\\"+lists_2[-1]+'_'+file_path[-1]
                # newfile = Tar+"\\"+lists_2[-1]+str(lists[0:-1])+"."+file_ext
                shutil.copy(path,newfile)
                self.textBrowser.append("<font color='#228B22'>"+"复制文件："+str(path)+" 到："+newfile+"  成功！"+"</font>")
                self.textBrowser.repaint()
        elif os.path.isdir(path):
            for x in os.listdir(path):
                self.ecopy(os.path.join(path, x),tar,tol_ext)
    def launcher(self,File_dir,Tar,string_get):
        """
            description: 进行复制前的判断工作
            return:
        """
        if (Tar == File_dir):
            self.textBrowser.append("<font color = 'red'>"+"目标路径与源路径相同，无需移动！"+"</font>")
        else:
            Tar=Tar.replace('/','\\')
            File_dir = File_dir.replace('/', '\\')
            tol_ext = string_get.split(" ")
            self.ecopy(File_dir,Tar,tol_ext)
            self.textBrowser.append("<font color='red'>"+"所有文件复制完成！"+"</font>")
    def run(self):
        """
            description: 获取变量值，调起启动器
            return:
        """
        src=self.lineEdit.text()
        tar=self.lineEdit2.text()
        kinds=self.lineEdit3.text()
        self.launcher(src,tar,kinds)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainui=mycopyui()
    mainui.show()
    sys.exit(app.exec_())