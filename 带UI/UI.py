# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\VanderWaals\source\VScode\Python\查找文件内容\带UI\文件内容查找.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
import os.path
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pushButton)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.textBrowser)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")

        MainWindow.setMenuBar(self.menuBar)

        self.actiondakai = QtWidgets.QAction(MainWindow)
        self.actiondakai.setObjectName("actiondakai")
        self.menu.addSeparator()
        self.menu.addAction(self.actiondakai)
        self.menu.addSeparator()
        self.menuBar.addAction(self.menu.menuAction())

        self.actiondakai.triggered.connect(self.openfile)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "文件内容查找"))
        self.label.setText(_translate("MainWindow", "输入文件路径"))
        self.label_2.setText(_translate("MainWindow", "输入关键字"))
        self.pushButton.setText(_translate("MainWindow", "点击查找！"))
        self.label_3.setText(_translate("MainWindow", "查找结果"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.actiondakai.setText(_translate("MainWindow", "打开"))

    def openfile(self):
        fm=QtWidgets.QFileDialog.getOpenFileName( self,"打开",'.',".doc;;.docx;;.xls;;.xlsx;;.txt")
        if fm[0]:
            self.lineEdit.setText(fm[0])
            self.textEdit.setText(  "检索使用正则表达式\n"
                                    "如果关键字包含英文符号: '.'、'*'、'?'"
                                    "请在其前面紧跟英文字符:'\\'")
    def tips(self,form):
        if form==0:
            QtWidgets.QMessageBox.warning(self,
                                    "错误",
                                    "不支持该类型文件",
                                    QtWidgets.QMessageBox.Ok
                                    )
            return 0
        else:
            return 1