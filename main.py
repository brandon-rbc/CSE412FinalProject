import math
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QTextEdit, QVBoxLayout, QScrollArea, QTableWidget
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
from PySide6.QtCore import QFile
import backend.psql_handlers as psql
import image_download


class UserHomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.currentUser = -1
        self.buttonList = []
        self.loginWindow = LoginWindow()
        self.searchWindow = SearchWindow()
        self.showWindow = ShowWindow()
        self.movieWindow = MovieWindow()
        self.loginWindow.loginButton.clicked.connect(self.updateUser)
        self.showWindow.ShowFavoriteButton.clicked.connect(self.updateShowFavorite)
        self.movieWindow.MovieFavoriteButton.clicked.connect(self.updateMovieFavorite)
        self.searchWindow.pushButton.clicked.connect(self.updateSearchOptions)

        self.currentUserFavorites = []


        self.setEnabled(True)
        self.resize(800, 600)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.MediaSearchButton = QPushButton(self.centralwidget, clicked=lambda: self.openSearchWindow())
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
        self.ChangeUserButton = QPushButton(self.centralwidget, clicked=lambda: self.openLoginWindow())
        # self.ChangeUserButton = QPushButton(self.centralwidget)
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
        self.gridLayout.setDefaultPositioning(2, Qt.Orientation.Horizontal)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QRect(20, 80, 401, 451))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


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
        self.SortByBox.currentIndexChanged.connect(self.updateUser)

        self.horizontalLayout.addWidget(self.SortByBox)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        self.updateUser()

        QMetaObject.connectSlotsByName(self)

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

    def openLoginWindow(self):
        self.loginWindow.show()

    def openSearchWindow(self):
        self.updateSearchOptions()
        self.searchWindow.show()

    def openShowWindow(self):
        button = self.sender()
        name = button.text()
        self.showWindow.setWindowTitle(name)
        self.showWindow.ShowTitleLabel.setText(f'Title: {name}')
        mediaID = psql.getMediaID(name)
        self.showWindow.mediaID = mediaID
        # print(self.showWindow.mediaID)
        if psql.checkInFavorites(self.currentUser, mediaID):
            self.showWindow.ShowFavoriteButton.setText('Remove from Favorites')
        else:
            self.showWindow.ShowFavoriteButton.setText('Add to Favorites')
        id, year, director, genres, numSeasons, numEpisdoes, synopsis, rating = psql.getShowInfo(name)
        year_string = f'Year of Release: {str(year)}'
        self.showWindow.ShowYearLabel.setText(year_string)
        director_string = f'Director: {director}'
        self.showWindow.ShowDirectorLabel.setText(director_string)
        genre_string = f'Genres: {str(genres)}'
        self.showWindow.ShowGenreLabel.setText(genre_string)
        self.showWindow.ShowSynopsisLabel.setText(synopsis)
        season_string = f'Number of Seasons: {numSeasons}'
        episode_string = f'Number of Episodes: {numEpisdoes}'
        self.showWindow.ShowNumSeasonsLabel.setText(season_string)
        self.showWindow.ShowNumEpisodesLabel.setText(episode_string)
        # Self..setFixedSize(200, 260)
        self.showWindow.ShowImageLabel.setPixmap(QPixmap(f'image_holder/{id}'))
        self.showWindow.ShowImageLabel.setScaledContents(True)
        self.showWindow.show()

    def openMovieWindow(self):
        button = self.sender()
        name = button.text()
        self.movieWindow.setWindowTitle(name)
        self.movieWindow.MovieTitleLabel.setText(f'Title: {name}')
        mediaID = psql.getMediaID(name)
        self.movieWindow.mediaID = mediaID
        if psql.checkInFavorites(self.currentUser, mediaID):
            self.movieWindow.MovieFavoriteButton.setText('Remove from Favorites')
        else:
            self.movieWindow.MovieFavoriteButton.setText('Add to Favorites')

        id, year, director, genres, runtime, synopsis, rating = psql.getMovieInfo(name)
        year_string = f'Year of Release: {str(year)}'
        self.movieWindow.MovieYearLabel.setText(year_string)
        director_string = f'Director: {director}'
        self.movieWindow.MovieDirectorLabel.setText(director_string)
        genre_string = f'Genres: {str(genres)}'
        self.movieWindow.MovieGenreLabel.setText(genre_string)
        self.movieWindow.MovieSynopsisLabel.setText(synopsis)
        runtime_string = f'Runtime: {runtime} min'
        self.movieWindow.label_3.setText(runtime_string)
        self.movieWindow.MovieImageLabel.setPixmap(QPixmap(f'image_holder/{id}'))
        self.movieWindow.MovieImageLabel.setScaledContents(True)

        self.movieWindow.show()

    def updateMovieFavorite(self):
        sender = self.sender()
        if sender.text() == 'Add to Favorites':
            psql.addFavorite(self.currentUser, self.movieWindow.mediaID)
            self.movieWindow.MovieFavoriteButton.setText('Remove from Favorites')
        elif sender.text() == 'Remove from Favorites':
            psql.removeFavorite(self.currentUser, self.movieWindow.mediaID)
            self.movieWindow.MovieFavoriteButton.setText('Add to Favorites')
        self.updateUser()

    def updateShowFavorite(self):
        sender = self.sender()
        if sender.text() == 'Add to Favorites':
            psql.addFavorite(self.currentUser, self.showWindow.mediaID)
            self.showWindow.ShowFavoriteButton.setText('Remove from Favorites')
        elif sender.text() == 'Remove from Favorites':
            psql.removeFavorite(self.currentUser, self.showWindow.mediaID)
            self.showWindow.ShowFavoriteButton.setText('Add to Favorites')
        self.updateUser()

    def updateUser(self):
        username = self.loginWindow.textEdit.toPlainText()
        age = self.loginWindow.textEdit_2.toPlainText()
        gender = self.loginWindow.textEdit_3.toPlainText()
        self.UserNameLabel.setText(username)
        self.AgeLabel.setText(age)
        self.GenderLabel.setText(gender)
        self.loginWindow.hide()
        sort_method = self.SortByBox.currentText()
        newUser, self.currentUserFavorites = psql.updateUserInfo(username, age, gender, sort_method)
        if self.currentUserFavorites:
            self.currentUser = newUser
        else:
            self.currentUser = newUser
        # print(f'current user: {self.currentUser}')

        #clear gridlayout
        num_delete = self.gridLayout.columnCount() * self.gridLayout.rowCount()
        for i in range(num_delete):
            if self.gridLayout.itemAt(i):
                self.gridLayout.itemAt(i).widget().deleteLater()

        for favorite in self.currentUserFavorites:
            media_image = QLabel(self.centralwidget)
            media_image.setObjectName(u"label")
            media_image.setFixedSize(200, 260)
            media_image.setPixmap(QPixmap(f'image_holder/{favorite[1]}'))
            media_image.setScaledContents(True)
            if favorite[3] == 'show':
                media_button = QPushButton(favorite[2])
                media_button.clicked.connect(self.openShowWindow)
            else:
                media_button = QPushButton(favorite[2])
                media_button.clicked.connect(self.openMovieWindow)
            media_button.setText(favorite[2])

            self.gridLayout.addWidget(media_image)
            self.gridLayout.addWidget(media_button)
        widget = QWidget()
        widget.setLayout(self.gridLayout)
        self.scrollArea.setWidget(widget)

    def updateSearchOptions(self):
        sort_method = self.searchWindow.SortByBoxSearch.currentText()
        search_method = self.searchWindow.SortByBoxSearch_2.currentText()
        search_query = self.searchWindow.textEdit.toPlainText()
        # print(sort_method, search_method, search_query)
        media = psql.getSearchMedia(sort_method, search_method, search_query)
        # print(media)

        # clear gridlayout
        # num_delete = self.gridLayout.count()
        # for i in range(num_delete):
        #     if self.searchWindow.gridLayout.itemAt(i):
        #         self.searchWindow.gridLayout.itemAt(i).widget().deleteLater()

        self.searchWindow.gridLayoutWidget = QWidget(self.centralwidget)
        self.searchWindow.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.searchWindow.gridLayoutWidget.setGeometry(QRect(20, 70, 761, 451))
        self.searchWindow.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.searchWindow.gridLayout.setObjectName(u"gridLayout")
        self.searchWindow.gridLayout.setContentsMargins(0, 0, 0, 0)

        widget = QWidget()
        widget.setLayout(self.searchWindow.gridLayout)
        self.searchWindow.scrollArea.setWidget(widget)
        for item in media:
            media_image = QLabel(self.centralwidget)
            media_image.setObjectName(u"label")
            media_image.setFixedSize(200, 260)
            media_image.setPixmap(QPixmap(f'image_holder/{item[2]}'))
            media_image.setScaledContents(True)
            if item[4] == 'show':
                media_button = QPushButton(item[0])
                media_button.clicked.connect(self.openShowWindow)
            else:
                media_button = QPushButton(item[0])
                media_button.clicked.connect(self.openMovieWindow)
            media_button.setText(item[0])

            self.searchWindow.gridLayout.addWidget(media_image)
            self.searchWindow.gridLayout.addWidget(media_button)
        widget = QWidget()
        widget.setLayout(self.searchWindow.gridLayout)
        self.searchWindow.scrollArea.setWidget(widget)


class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(803, 587)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 70, 761, 451))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QRect(20, 70, 761, 451))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(320, 20, 451, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout_2.addWidget(self.textEdit)

        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.SortByBoxSearch_2 = QComboBox(self.horizontalLayoutWidget)
        self.SortByBoxSearch_2.addItem("")
        self.SortByBoxSearch_2.addItem("")
        self.SortByBoxSearch_2.addItem("")
        self.SortByBoxSearch_2.setObjectName(u"SortByBoxSearch_2")

        self.horizontalLayout_2.addWidget(self.SortByBoxSearch_2)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 20, 111, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)

        self.horizontalLayout.addWidget(self.label_6)

        self.SortByBoxSearch = QComboBox(self.horizontalLayoutWidget_2)
        self.SortByBoxSearch.addItem("")
        self.SortByBoxSearch.addItem("")
        self.SortByBoxSearch.setObjectName(u"SortByBoxSearch")

        self.horizontalLayout.addWidget(self.SortByBoxSearch)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 803, 22))
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        # setupUi

    def retranslateUi(self, SearchWindow):
        SearchWindow.setWindowTitle(QCoreApplication.translate("SearchWindow", u"Search Media", None))
        self.pushButton.setText(QCoreApplication.translate("SearchWindow", u"Search", None))
        self.label.setText(QCoreApplication.translate("SearchWindow", u"Search By:", None))
        self.SortByBoxSearch_2.setItemText(0, QCoreApplication.translate("SearchWindow", u"Title", None))
        self.SortByBoxSearch_2.setItemText(1, QCoreApplication.translate("SearchWindow", u"Director", None))
        self.SortByBoxSearch_2.setItemText(2, QCoreApplication.translate("SearchWindow", u"Genre", None))

        self.label_6.setText(QCoreApplication.translate("SearchWindow", u"Sort By:", None))
        self.SortByBoxSearch.setItemText(0, QCoreApplication.translate("SearchWindow", u"Rating", None))
        self.SortByBoxSearch.setItemText(1, QCoreApplication.translate("SearchWindow", u"A-Z", None))

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(261, 138)
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
        # self.loginButton = QPushButton(LoginWindow, clicked=lambda: self.updateUser())
        self.loginButton = QPushButton(self)
        self.loginButton.setObjectName(u"pushButton")
        self.loginButton.setGeometry(QRect(170, 110, 75, 24))
        # self.loginButton.clicked.connect(self.updateUser)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"User Info", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"Username:", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"Age:", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"Gender:", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWindow", u"Log In", None))

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

class MovieWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mediaID = -1
        self.resize(416, 490)
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

if __name__ == "__main__":
    psql.main()
    image_download.downloadImages()
    app = QApplication(sys.argv)
    userWindow = UserHomePage()
    userWindow.show()
    sys.exit((app.exec()))
