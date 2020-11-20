# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '文件复制.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 586)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setObjectName("label1")
        self.horizontalLayout.addWidget(self.label1)
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setObjectName("label2")
        self.gridLayout.addWidget(self.label2, 1, 0, 1, 1)
        self.label3 = QtWidgets.QLabel(self.centralwidget)
        self.label3.setObjectName("label3")
        self.gridLayout.addWidget(self.label3, 2, 0, 1, 1)
        self.label4 = QtWidgets.QLabel(self.centralwidget)
        self.label4.setObjectName("label4")
        self.gridLayout_2.addWidget(self.label4, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(82, 230, 72, 15))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit2.setObjectName("lineEdit2")
        self.gridLayout.addWidget(self.lineEdit2, 1, 1, 1, 1)
        self.lineEdit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit3.setObjectName("lineEdit3")
        self.gridLayout.addWidget(self.lineEdit3, 2, 1, 1, 2)

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayout.addWidget(self.pushButton1, 3, 0, 1, 3)
        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setObjectName("pushButton2")
        self.horizontalLayout.addWidget(self.pushButton2)
        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setObjectName("pushButton3")
        self.gridLayout.addWidget(self.pushButton3, 1, 2, 1, 1)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_2.addWidget(self.textBrowser, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionhelp = QtWidgets.QAction(MainWindow)
        self.actionhelp.setObjectName("actionhelp")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">源文件目录</span></p></body></html>"))
        self.pushButton2.setText(_translate("MainWindow", "浏览"))
        self.label2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">目标目录</span></p></body></html>"))
        self.pushButton3.setText(_translate("MainWindow", "浏览"))
        self.label3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">文件类型</span></p></body></html>"))
        self.pushButton1.setText(_translate("MainWindow", "开始"))
        self.label4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">使用说明：</span></p><p><span style=\" font-size:10pt;\">1.输入源文件目录；</span></p><p><span style=\" font-size:10pt;\">2.输入目标目录；</span></p><p><span style=\" font-size:10pt;\">3.输入要批量复制的文件扩展后缀名(如: jpg);</span></p><p><span style=\" font-size:10pt;\">4.多个类型以空格分隔。</span></p></body></html>"))
        self.actionhelp.setText(_translate("MainWindow", "说明"))
