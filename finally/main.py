"""
    Description:主窗口
    Autor:
    Date: 2020-06-13 15:25:57
    LastEditTime: 2020-06-13 15:25:57
    LastEditors:
"""
import sys
from functools import partial
from PyQt5.QtWidgets import *
from logic import logiccopy
from logic import logicmain
from logic import logicfind


if __name__ == "__main__":
    app=QApplication(sys.argv)
    MainWindow=QMainWindow()
    ui1=logicmain.mymain()
    ui1.setupUi(MainWindow)
    #两个子窗口类
    ui2=logiccopy.mycopyui()
    ui3=logicfind.myfind()
    #绑定按键
    ui1.selfind.clicked.connect(ui3.show)
    ui1.selcopy.clicked.connect(ui2.show)
    ui1.actionzhizuo.triggered.connect(ui1.Information)
    MainWindow.show()
    sys.exit(app.exec_())