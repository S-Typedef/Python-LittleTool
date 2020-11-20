"""
    Description: 设置主窗口界面并绑定按键
    Autor:
    Date: 2020-06-13 17:43:07
    LastEditTime: 2020-06-13 17:43:07
    LastEditors:
"""
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from ui import uimain
class mymain(uimain.Ui_MainWindow):
    def __init__(self):
        """
            description: 初始化，并绑定按键
            return:
        """
        super().__init__()
        self.setupUi(self)
        self.autorname=""
        self.autornumber=""
        self.actionzhizuo.triggered.connect(self.Information)
    def Information(self):
        """
            description: 弹出消息窗口，显示制作信息
            return:
        """
        reply=QMessageBox.information(
            self,
            "关于",
            "制作人：\n{0}\n{1}".format(self.autorname,self.autornumber),
            QMessageBox.Yes
        )
if __name__ == "__main__":
    app=QApplication(sys.argv)
    mainui=mymain()
    mainui.show()
    sys.exit(app.exec_())