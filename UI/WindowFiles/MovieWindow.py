# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MovieWindow.ui'
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

class Ui_MovieWindow(object):
    def setupUi(self, MovieWindow):
        if not MovieWindow.objectName():
            MovieWindow.setObjectName(u"MovieWindow")
        MovieWindow.resize(416, 490)
        self.MovieImageLabel = QLabel(MovieWindow)
        self.MovieImageLabel.setObjectName(u"MovieImageLabel")
        self.MovieImageLabel.setGeometry(QRect(100, 20, 201, 221))
        self.verticalLayoutWidget = QWidget(MovieWindow)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 270, 161, 151))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.MovieTitleLabel = QLabel(self.verticalLayoutWidget)
        self.MovieTitleLabel.setObjectName(u"MovieTitleLabel")

        self.verticalLayout.addWidget(self.MovieTitleLabel)

        self.MovieYearLabel = QLabel(self.verticalLayoutWidget)
        self.MovieYearLabel.setObjectName(u"MovieYearLabel")

        self.verticalLayout.addWidget(self.MovieYearLabel)

        self.MovieDirectorLabel = QLabel(self.verticalLayoutWidget)
        self.MovieDirectorLabel.setObjectName(u"MovieDirectorLabel")

        self.verticalLayout.addWidget(self.MovieDirectorLabel)

        self.MovieGenreLabel = QLabel(self.verticalLayoutWidget)
        self.MovieGenreLabel.setObjectName(u"MovieGenreLabel")

        self.verticalLayout.addWidget(self.MovieGenreLabel)

        self.MovieNumSeasonsLabel = QLabel(self.verticalLayoutWidget)
        self.MovieNumSeasonsLabel.setObjectName(u"MovieNumSeasonsLabel")

        self.verticalLayout.addWidget(self.MovieNumSeasonsLabel)

        self.MovieNumEpisodesLabel = QLabel(self.verticalLayoutWidget)
        self.MovieNumEpisodesLabel.setObjectName(u"MovieNumEpisodesLabel")

        self.verticalLayout.addWidget(self.MovieNumEpisodesLabel)

        self.label = QLabel(MovieWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 250, 49, 16))
        self.MovieSynopsisLabel = QLabel(MovieWindow)
        self.MovieSynopsisLabel.setObjectName(u"MovieSynopsisLabel")
        self.MovieSynopsisLabel.setGeometry(QRect(200, 270, 151, 151))
        self.FavoriteButton = QPushButton(MovieWindow)
        self.FavoriteButton.setObjectName(u"FavoriteButton")
        self.FavoriteButton.setGeometry(QRect(150, 440, 111, 31))

        self.retranslateUi(MovieWindow)

        QMetaObject.connectSlotsByName(MovieWindow)
    # setupUi

    def retranslateUi(self, MovieWindow):
        MovieWindow.setWindowTitle(QCoreApplication.translate("MovieWindow", u"Form", None))
        self.MovieImageLabel.setText(QCoreApplication.translate("MovieWindow", u"MovieImageLabel", None))
        self.MovieTitleLabel.setText(QCoreApplication.translate("MovieWindow", u"Title:", None))
        self.MovieYearLabel.setText(QCoreApplication.translate("MovieWindow", u"Year of Release:", None))
        self.MovieDirectorLabel.setText(QCoreApplication.translate("MovieWindow", u"Director:", None))
        self.MovieGenreLabel.setText(QCoreApplication.translate("MovieWindow", u"Genres:", None))
        self.MovieNumSeasonsLabel.setText(QCoreApplication.translate("MovieWindow", u"Number of Seasons:", None))
        self.MovieNumEpisodesLabel.setText(QCoreApplication.translate("MovieWindow", u"Number of Episodes:", None))
        self.label.setText(QCoreApplication.translate("MovieWindow", u"Synopsis", None))
        self.MovieSynopsisLabel.setText(QCoreApplication.translate("MovieWindow", u"SynopsisLabel", None))
        self.FavoriteButton.setText(QCoreApplication.translate("MovieWindow", u"Add to Favorites", None))
    # retranslateUi

