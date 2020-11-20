# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\VanderWaals\source\VScode\Python\查找文件内容\UI\查找.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.centralwidget)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.splitter_2)
        self.textBrowser.setObjectName("textBrowser")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton2.setObjectName("pushButton2")
        self.gridLayout.addWidget(self.pushButton2, 3, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit2.setObjectName("lineEdit2")
        self.gridLayout.addWidget(self.lineEdit2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton1 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton1.setObjectName("pushButton1")
        self.gridLayout.addWidget(self.pushButton1, 2, 0, 1, 2)
        self.lineEdit1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit1.setObjectName("lineEdit1")
        self.gridLayout.addWidget(self.lineEdit1, 0, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondakai = QtWidgets.QAction(MainWindow)
        self.actiondakai.setObjectName("actiondakai")
        self.menu.addAction(self.actiondakai)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton2.setText(_translate("MainWindow", "绘制词云"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">关键字</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#ff0000;\">文件</span></p></body></html>"))
        self.pushButton1.setText(_translate("MainWindow", "查找"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">1.按下查找键</span></p><p><span style=\" font-size:11pt; color:#ff0000;\">(1)使用正则表达式进行查找</span></p><p><span style=\" font-size:11pt; color:#ff0000;\">(2)按段落输出字符</span></p><p><span style=\" font-size:11pt; color:#ff0000;\">(3)以&quot; &quot;&quot; &quot;包围</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt; color:#ff0000;\">2.按下绘制词云键</span></p><p><span style=\" font-size:11pt; color:#ff0000;\">(1)文件内容按词频输出图片</span></p><p><span style=\" font-size:11pt; color:#ff0000;\">(2)关键字输入栏内容作为文件名</span></p><p><span style=\" font-size:11pt; color:#ff0000;\">(3)图片保存至程序运行目录下</span></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.actiondakai.setText(_translate("MainWindow", "打开"))
