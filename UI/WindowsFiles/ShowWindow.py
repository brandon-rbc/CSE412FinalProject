from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)

from PySide6.QtWidgets import (QLabel, QMainWindow, QPushButton, QWidget)

class ShowWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mediaID = -1
        self.resize(429, 486)
        self.ShowImageLabel = QLabel(self)
        self.ShowImageLabel.setObjectName(u"ShowImageLabel")
        self.ShowImageLabel.setGeometry(QRect(135, 10, 180, 221))
        self.ShowFavoriteButton = QPushButton(self)
        self.ShowFavoriteButton.setObjectName(u"FavoriteButton")
        self.ShowFavoriteButton.setGeometry(QRect(160, 440, 111, 31))
        self.verticalLayoutWidget = QWidget(self)
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

        self.ShowNumSeasonsLabel = QLabel(self.verticalLayoutWidget)
        self.ShowNumSeasonsLabel.setObjectName(u"ShowNumSeasonsLabel")

        self.verticalLayout_2.addWidget(self.ShowNumSeasonsLabel)

        self.ShowNumEpisodesLabel = QLabel(self.verticalLayoutWidget)
        self.ShowNumEpisodesLabel.setObjectName(u"ShowNumEpisodesLabel")

        self.verticalLayout_2.addWidget(self.ShowNumEpisodesLabel)

        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 240, 49, 16))
        self.ShowSynopsisLabel = QLabel(self)
        self.ShowSynopsisLabel.setObjectName(u"ShowSynopsisLabel")
        self.ShowSynopsisLabel.setGeometry(QRect(240, 260, 151, 151))

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self, S):
        S.setWindowTitle(QCoreApplication.translate("S", u"Show", None))
        self.ShowFavoriteButton.setText(QCoreApplication.translate("S", u"Add to Favorites", None))
        self.ShowTitleLabel.setText(QCoreApplication.translate("S", u"Title:", None))
        self.ShowYearLabel.setText(QCoreApplication.translate("S", u"Year of Release:", None))
        self.ShowDirectorLabel.setText(QCoreApplication.translate("S", u"Director:", None))
        self.ShowGenreLabel.setText(QCoreApplication.translate("S", u"Genres:", None))
        self.ShowNumSeasonsLabel.setText(QCoreApplication.translate("MovieWindow", u"Number of Seasons:", None))
        self.ShowNumEpisodesLabel.setText(QCoreApplication.translate("MovieWindow", u"Number of Episodes:", None))
        self.label.setText(QCoreApplication.translate("S", u"Synopsis", None))
        self.ShowSynopsisLabel.setText(QCoreApplication.translate("S", u"SynopsisLabel", None))