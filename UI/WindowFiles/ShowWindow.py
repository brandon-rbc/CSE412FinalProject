# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShowWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_S(object):
    def setupUi(self, S):
        if not S.objectName():
            S.setObjectName(u"S")
        S.resize(429, 486)
        self.ShowImageLabel = QLabel(S)
        self.ShowImageLabel.setObjectName(u"ShowImageLabel")
        self.ShowImageLabel.setGeometry(QRect(140, 10, 201, 221))
        self.FavoriteButton = QPushButton(S)
        self.FavoriteButton.setObjectName(u"FavoriteButton")
        self.FavoriteButton.setGeometry(QRect(160, 440, 111, 31))
        self.verticalLayoutWidget = QWidget(S)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 270, 161, 131))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.ShowTitleLabel = QLabel(self.verticalLayoutWidget)
        self.ShowTitleLabel.setObjectName(u"ShowTitleLabel")

        self.verticalLayout_2.addWidget(self.ShowTitleLabel)

        self.ShowYearLabel = QLabel(self.verticalLayoutWidget)
        self.ShowYearLabel.setObjectName(u"ShowYearLabel")

        self.verticalLayout_2.addWidget(self.ShowYearLabel)

        self.ShowDirectorLabel = QLabel(self.verticalLayoutWidget)
        self.ShowDirectorLabel.setObjectName(u"ShowDirectorLabel")

        self.verticalLayout_2.addWidget(self.ShowDirectorLabel)

        self.ShowGenreLabel = QLabel(self.verticalLayoutWidget)
        self.ShowGenreLabel.setObjectName(u"ShowGenreLabel")

        self.verticalLayout_2.addWidget(self.ShowGenreLabel)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label = QLabel(S)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 240, 49, 16))
        self.ShowSynopsisLabel = QLabel(S)
        self.ShowSynopsisLabel.setObjectName(u"ShowSynopsisLabel")
        self.ShowSynopsisLabel.setGeometry(QRect(240, 260, 151, 151))

        self.retranslateUi(S)

        QMetaObject.connectSlotsByName(S)
    # setupUi

    def retranslateUi(self, S):
        S.setWindowTitle(QCoreApplication.translate("S", u"Form", None))
        self.ShowImageLabel.setText(QCoreApplication.translate("S", u"ShowImageLabel", None))
        self.FavoriteButton.setText(QCoreApplication.translate("S", u"Add to Favorites", None))
        self.ShowTitleLabel.setText(QCoreApplication.translate("S", u"Title:", None))
        self.ShowYearLabel.setText(QCoreApplication.translate("S", u"Year of Release:", None))
        self.ShowDirectorLabel.setText(QCoreApplication.translate("S", u"Director:", None))
        self.ShowGenreLabel.setText(QCoreApplication.translate("S", u"Genres:", None))
        self.label_3.setText(QCoreApplication.translate("S", u"Runtime:", None))
        self.label.setText(QCoreApplication.translate("S", u"Synopsis", None))
        self.ShowSynopsisLabel.setText(QCoreApplication.translate("S", u"SynopsisLabel", None))
    # retranslateUi

