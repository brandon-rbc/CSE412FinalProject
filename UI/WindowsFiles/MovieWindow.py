from PySide6.QtGui import Qt
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QThreadPool)

from PySide6.QtWidgets import (QLabel, QMainWindow, QPushButton,QWidget, QScrollArea)

windowWidth = 450
windowHeight = 490
class MovieWindow(QMainWindow):
    #initializes all elements of MovieWindow including UI
    def __init__(self):
        super().__init__()
        self.mediaID = -1
        self.setFixedSize(windowWidth, windowHeight)
        self.setObjectName(u"movieWindow")
        self.MovieImageLabel = QLabel(self)
        self.MovieImageLabel.setObjectName(u"MovieImageLabel")
        self.MovieImageLabel.setGeometry(QRect((windowWidth/2)-(180/2), 10, 180, 221))
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect((windowWidth/4) - 100, 250, 200, 151))
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

        self.MovieRatingLabel = QLabel(self.verticalLayoutWidget)
        self.MovieRatingLabel.setObjectName(u"MovieRatingLabel")

        self.verticalLayout.addWidget(self.MovieRatingLabel)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(((3/4) * windowWidth) - 25, 250, 50, 16))
       
        self.MovieSynopsisLabel = QLabel(self)
        self.MovieSynopsisLabel.setObjectName(u"MovieSynopsisLabel")
        self.MovieSynopsisLabel.setGeometry(QRect(((3/4) * windowWidth) - 75, 260, 150, 150))
        self.MovieSynopsisLabel.setWordWrap(True)

        self.MovieFavoriteButton = QPushButton(self)
        self.MovieFavoriteButton.setObjectName(u"FavoriteButton")
        self.MovieFavoriteButton.setGeometry(QRect((windowWidth/2)-(200/2), 440, 200, 31))

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        # setupUi

    #qtdesigner generated code
    def retranslateUi(self, MovieWindow):
        MovieWindow.setWindowTitle(QCoreApplication.translate("MovieWindow", u"Movie", None))
        self.MovieTitleLabel.setText(QCoreApplication.translate("MovieWindow", u"Title:", None))
        self.MovieYearLabel.setText(QCoreApplication.translate("MovieWindow", u"Year of Release:", None))
        self.MovieDirectorLabel.setText(QCoreApplication.translate("MovieWindow", u"Director:", None))
        self.MovieGenreLabel.setText(QCoreApplication.translate("MovieWindow", u"Genres:", None))
        self.MovieRatingLabel.setText(QCoreApplication.translate("MovieWindow", u"Rating:", None))
        self.label.setText(QCoreApplication.translate("MovieWindow", u"Synopsis", None))
        self.label_3.setText(QCoreApplication.translate("S", u"Runtime:", None))
        self.MovieSynopsisLabel.setText(QCoreApplication.translate("MovieWindow", u"SynopsisLabel", None))
        self.MovieFavoriteButton.setText(QCoreApplication.translate("MovieWindow", u"Add to Favorites", None))