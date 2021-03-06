from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QLabel, QMainWindow, QPushButton)

class LoginWindow(QMainWindow):
    #initializes all elements of LoginWindow including UI
    def __init__(self):
        super().__init__()
        self.setFixedSize(261, 138)
        self.setObjectName("loginWindow")
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 10, 49, 16))
        self.textEdit = QTextEdit(self)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(80, 40, 141, 21))
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setText('bccampos')
        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 61, 21))
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 70, 31, 16))
        self.textEdit_2 = QTextEdit(self)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(80, 70, 41, 21))
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_2.setText('21')
        self.label_4 = QLabel(self)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 70, 41, 16))
        self.textEdit_3 = QTextEdit(self)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(180, 70, 41, 21))
        self.textEdit_3.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_3.setText('m')
        self.loginButton = QPushButton(self)
        self.loginButton.setObjectName(u"pushButton")
        self.loginButton.setGeometry(QRect(170, 110, 75, 24))

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

    #qtdesigner generated code
    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"User Info", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"Username:", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"Age:", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"Gender:", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWindow", u"Log In", None))