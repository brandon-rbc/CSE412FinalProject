from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)

from PySide6.QtWidgets import (QLabel, QMainWindow, QPushButton,QWidget, QScrollArea)


class MovieWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mediaID = -1
        self.setFixedSize(416, 490)
        self.MovieImageLabel = QLabel(self)
        self.MovieImageLabel.setObjectName(u"MovieImageLabel")
        self.MovieImageLabel.setGeometry(QRect(135, 10, 180, 221))
        self.verticalLayoutWidget = QWidget(self)
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

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 250, 49, 16))

        

        self.MovieSynopsisLabel = QLabel(self)
        self.MovieSynopsisLabel.setObjectName(u"MovieSynopsisLabel")
        self.MovieSynopsisLabel.setGeometry(QRect(200, 270, 151, 151))
        self.MovieSynopsisLabel.setWordWrap(True)

        
        self.MovieFavoriteButton = QPushButton(self)
        self.MovieFavoriteButton.setObjectName(u"FavoriteButton")
        self.MovieFavoriteButton.setGeometry(QRect(150, 440, 111, 31))

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        # setupUi

    def retranslateUi(self, MovieWindow):
        MovieWindow.setWindowTitle(QCoreApplication.translate("MovieWindow", u"Movie", None))
        self.MovieTitleLabel.setText(QCoreApplication.translate("MovieWindow", u"Title:", None))
        self.MovieYearLabel.setText(QCoreApplication.translate("MovieWindow", u"Year of Release:", None))
        self.MovieDirectorLabel.setText(QCoreApplication.translate("MovieWindow", u"Director:", None))
        self.MovieGenreLabel.setText(QCoreApplication.translate("MovieWindow", u"Genres:", None))
        self.label.setText(QCoreApplication.translate("MovieWindow", u"Synopsis", None))
        self.label_3.setText(QCoreApplication.translate("S", u"Runtime:", None))
        self.MovieSynopsisLabel.setText(QCoreApplication.translate("MovieWindow", u"SynopsisLabel", None))
        self.MovieFavoriteButton.setText(QCoreApplication.translate("MovieWindow", u"Add to Favorites", None))