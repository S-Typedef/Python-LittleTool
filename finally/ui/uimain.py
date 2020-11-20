# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '主窗口.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(714, 556)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 80, 41, 261))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(250, 80, 191, 291))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.selfind = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selfind.setFont(font)
        self.selfind.setObjectName("selfind")
        self.selcopy = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selcopy.setFont(font)
        self.selcopy.setObjectName("selcopy")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 714, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionzhizuo = QtWidgets.QAction(MainWindow)
        self.actionzhizuo.setObjectName("actionzhizuo")
        self.menu.addAction(self.actionzhizuo)
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "简易工具箱"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">功</span></p><p><span style=\" font-size:16pt;\">能</span></p><p><span style=\" font-size:16pt;\">选</span></p><p><span style=\" font-size:16pt;\">择</span></p></body></html>"))
        self.selfind.setText(_translate("MainWindow", "文件内容查找"))
        self.selcopy.setText(_translate("MainWindow", "文件批量复制"))
        self.menu.setTitle(_translate("MainWindow", "关于"))
        self.actionzhizuo.setText(_translate("MainWindow", "制作"))
