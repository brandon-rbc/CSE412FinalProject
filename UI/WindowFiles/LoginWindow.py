# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
                               QTextEdit, QWidget, QMainWindow)
# from UI.WindowFiles.UserWindow import Ui_UserHomePage
import backend.psql_handlers as psql

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(261, 138)
        self.label = QLabel(LoginWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 10, 49, 16))
        self.textEdit = QTextEdit(LoginWindow)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(80, 40, 141, 21))
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_2 = QLabel(LoginWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 61, 21))
        self.label_3 = QLabel(LoginWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 70, 31, 16))
        self.textEdit_2 = QTextEdit(LoginWindow)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(80, 70, 41, 21))
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.label_4 = QLabel(LoginWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 70, 41, 16))
        self.textEdit_3 = QTextEdit(LoginWindow)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(180, 70, 41, 21))
        self.textEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.loginButton = QPushButton(LoginWindow, clicked=lambda: self.updateUser())
        self.loginButton = QPushButton()
        self.loginButton.setObjectName(u"pushButton")
        self.loginButton.setGeometry(QRect(170, 110, 75, 24))
        # self.loginButton.clicked.connect(self.updateUser)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Form", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"User Info", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"Username:", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"Age:", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"Gender:", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWindow", u"Log In", None))
    # retranslateUi


    def updateUser(self):
        username = self.textEdit.toPlainText()
        age = self.textEdit_2.toPlainText()
        gender = self.textEdit_3.toPlainText()
        print(username, age, gender)
        # Ui_UserHomePage.UserNameLabel.setText(username)
        # psql.updateUserInfo(username=username, age=age, gender=gender)
        # UserWindow.UserName

