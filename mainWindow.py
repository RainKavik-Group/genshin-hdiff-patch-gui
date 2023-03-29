# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QCommandLinkButton, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPlainTextEdit, QSizePolicy, QStatusBar, QToolButton,
    QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 717)
        icon = QIcon()
        icon.addFile(u":/pic/RoundCorner.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(200, 180, 121, 41))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(11)
        self.commandLinkButton.setFont(font)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 240, 511, 431))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(9)
        self.plainTextEdit.setFont(font1)
        self.plainTextEdit.setReadOnly(True)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 40, 481, 22))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(11)
        self.label.setFont(font2)

        self.horizontalLayout.addWidget(self.label)

        self.path50_textbox = QLineEdit(self.layoutWidget)
        self.path50_textbox.setObjectName(u"path50_textbox")
        self.path50_textbox.setEchoMode(QLineEdit.Normal)
        self.path50_textbox.setReadOnly(True)

        self.horizontalLayout.addWidget(self.path50_textbox)

        self.path50_button = QToolButton(self.layoutWidget)
        self.path50_button.setObjectName(u"path50_button")

        self.horizontalLayout.addWidget(self.path50_button)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 90, 481, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.path51_textbox = QLineEdit(self.layoutWidget1)
        self.path51_textbox.setObjectName(u"path51_textbox")
        self.path51_textbox.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.path51_textbox)

        self.path51_button = QToolButton(self.layoutWidget1)
        self.path51_button.setObjectName(u"path51_button")

        self.horizontalLayout_2.addWidget(self.path51_button)

        self.layoutWidget_2 = QWidget(self.centralwidget)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 140, 481, 26))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.layoutWidget_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setFont(font2)

        self.horizontalLayout_3.addWidget(self.checkBox)

        self.pathAudio_textbox = QLineEdit(self.layoutWidget_2)
        self.pathAudio_textbox.setObjectName(u"pathAudio_textbox")
        self.pathAudio_textbox.setEnabled(False)
        self.pathAudio_textbox.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.pathAudio_textbox)

        self.pathAudio_button = QToolButton(self.layoutWidget_2)
        self.pathAudio_button.setObjectName(u"pathAudio_button")
        self.pathAudio_button.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.pathAudio_button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5dee\u5206\u5305\u5408\u5e76 For \u67d0\u52a8\u6f2b\u6e38\u620f  |  Copyright by RainKavik", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u5408\u5e76\uff01", None))
        self.plainTextEdit.setPlainText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5b8c\u6574\u5ba2\u6237\u7aef\u8def\u5f84\uff1a", None))
        self.path50_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u6e38\u620f\u5dee\u5206\u5305\u8def\u5f84\uff1a", None))
        self.path51_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u97f3\u5dee\u5206\u5305\uff1a  ", None))
        self.pathAudio_button.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

