# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UserWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
from UI.WindowFiles.SearchWindow import Ui_SearchWindow
from UI.WindowFiles.LoginWindow import Ui_LoginWindow
import backend.psql_handlers as psql

class Ui_UserHomePage(object):

    # def openSearchWindow(self):
    #     self.window = QMainWindow()
    #     self.ui = Ui_SearchWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    #
    # def openLoginWindow(self):
    #     self.window = QMainWindow()
    #     self.ui = Ui_LoginWindow()
    #     self.ui.setupUi(self.window)
    #     self.window.show()



    def setupUi(self, UserHomePage):
        if not UserHomePage.objectName():
            UserHomePage.setObjectName(u"UserHomePage")
        UserHomePage.setEnabled(True)
        UserHomePage.resize(800, 600)
        self.centralwidget = QWidget(UserHomePage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MediaSearchButton = QPushButton()
        # self.MediaSearchButton = QPushButton(self.centralwidget, clicked=lambda: self.openSearchWindow())
        self.MediaSearchButton.setObjectName(u"MediaSearchButton")
        self.MediaSearchButton.setGeometry(QRect(320, 20, 101, 31))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(560, 120, 181, 181))
        self.label.setStyleSheet(u"QLabel {\n"
"	background-image: url(Assets/ProfileImage.png)\n"
"}")
        self.label.setPixmap(QPixmap(u"../../Assets/ProfileImage.jpg"))
        self.label.setScaledContents(True)
        self.UserNameLabel = QLabel(self.centralwidget)
        self.UserNameLabel.setObjectName(u"UserNameLabel")
        self.UserNameLabel.setGeometry(QRect(600, 300, 91, 20))
        # self.ChangeUserButton = QPushButton(self.centralwidget, clicked=lambda: self.openLoginWindow())
        self.ChangeUserButton = QPushButton(self.centralwidget)
        self.ChangeUserButton.setObjectName(u"ChangeUserButton")
        self.ChangeUserButton.setGeometry(QRect(610, 320, 75, 24))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(600, 360, 31, 16))
        self.AgeLabel = QLabel(self.centralwidget)
        self.AgeLabel.setObjectName(u"AgeLabel")
        self.AgeLabel.setGeometry(QRect(630, 360, 49, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 60, 51, 16))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(580, 380, 51, 16))
        self.GenderLabel = QLabel(self.centralwidget)
        self.GenderLabel.setObjectName(u"GenderLabel")
        self.GenderLabel.setGeometry(QRect(630, 380, 71, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(550, 400, 81, 16))
        self.NumFavsLabel = QLabel(self.centralwidget)
        self.NumFavsLabel.setObjectName(u"NumFavsLabel")
        self.NumFavsLabel.setGeometry(QRect(630, 400, 51, 16))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 80, 491, 451))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 108, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)

        self.horizontalLayout.addWidget(self.label_6)

        self.SortByBox = QComboBox(self.horizontalLayoutWidget)
        self.SortByBox.addItem("")
        self.SortByBox.addItem("")
        self.SortByBox.setObjectName(u"SortByBox")
        # self.SortByBox.currentIndexChanged.connect(self.updateMedia)

        self.horizontalLayout.addWidget(self.SortByBox)

        UserHomePage.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(UserHomePage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        UserHomePage.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(UserHomePage)
        self.statusbar.setObjectName(u"statusbar")
        UserHomePage.setStatusBar(self.statusbar)

        self.retranslateUi(UserHomePage)

        QMetaObject.connectSlotsByName(UserHomePage)
    # setupUi

    def retranslateUi(self, UserHomePage):
        UserHomePage.setWindowTitle(QCoreApplication.translate("UserHomePage", u"User Page", None))
        self.MediaSearchButton.setText(QCoreApplication.translate("UserHomePage", u"Search Media", None))
        self.label.setText("")
        self.UserNameLabel.setText(QCoreApplication.translate("UserHomePage", u"USERNAME HERE", None))
        self.ChangeUserButton.setText(QCoreApplication.translate("UserHomePage", u"Not You?", None))
        self.label_2.setText(QCoreApplication.translate("UserHomePage", u"Age: ", None))
        self.AgeLabel.setText(QCoreApplication.translate("UserHomePage", u"AgeLabel", None))
        self.label_4.setText(QCoreApplication.translate("UserHomePage", u"Favorites", None))
        self.label_5.setText(QCoreApplication.translate("UserHomePage", u"Gender:", None))
        self.GenderLabel.setText(QCoreApplication.translate("UserHomePage", u"GenderLabel", None))
        self.label_3.setText(QCoreApplication.translate("UserHomePage", u"# of Favorites:", None))
        self.NumFavsLabel.setText(QCoreApplication.translate("UserHomePage", u"NumFavs", None))
        self.label_6.setText(QCoreApplication.translate("UserHomePage", u"Sort By:", None))
        self.SortByBox.setItemText(0, QCoreApplication.translate("UserHomePage", u"Rating", None))
        self.SortByBox.setItemText(1, QCoreApplication.translate("UserHomePage", u"A-Z", None))

    # retranslateUi

    def updateUser(self):
        self.UserNameLabel.setText()

    def updateMedia(self):
        currentSort = self.SortByBox.currentText()
        print(f'current sorting method: {currentSort}')
