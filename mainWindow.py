# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(531, 429)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/RoundCorner.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(200, 130, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 180, 511, 201))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 481, 22))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.path50_textbox = QtWidgets.QLineEdit(self.layoutWidget)
        self.path50_textbox.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.path50_textbox.setReadOnly(True)
        self.path50_textbox.setObjectName("path50_textbox")
        self.horizontalLayout.addWidget(self.path50_textbox)
        self.path50_button = QtWidgets.QToolButton(self.layoutWidget)
        self.path50_button.setObjectName("path50_button")
        self.horizontalLayout.addWidget(self.path50_button)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(60, 90, 451, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.path51_textbox = QtWidgets.QLineEdit(self.layoutWidget1)
        self.path51_textbox.setReadOnly(True)
        self.path51_textbox.setObjectName("path51_textbox")
        self.horizontalLayout_2.addWidget(self.path51_textbox)
        self.path51_button = QtWidgets.QToolButton(self.layoutWidget1)
        self.path51_button.setObjectName("path51_button")
        self.horizontalLayout_2.addWidget(self.path51_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "差分包合并 For 某动漫游戏  |  Copyright by RainKavik"))
        self.commandLinkButton.setText(_translate("MainWindow", "开始合并！"))
        self.label.setText(_translate("MainWindow", "完整客户端路径："))
        self.path50_button.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "差分包路径："))
        self.path51_button.setText(_translate("MainWindow", "..."))
import resources_rc