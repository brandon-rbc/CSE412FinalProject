from PySide6.QtWidgets import QMenu, QScrollArea
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QPixmap, QFont, QPainter, QBrush, QPen, QLinearGradient, QPalette, QColor)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton, QStatusBar, QWidget)

import backend.psql_handlers as psql
from UI.WindowsFiles.SearchWindow import SearchWindow
from UI.WindowsFiles.LoginWindow import LoginWindow
from UI.WindowsFiles.MovieWindow import MovieWindow
from UI.WindowsFiles.ShowWindow import ShowWindow


class UserHomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.currentUser = -1
        self.buttonList = []
        self.loginWindow = LoginWindow()
        self.searchWindow = SearchWindow()
        self.showWindow = ShowWindow()
        self.movieWindow = MovieWindow()
        self._createMenuBar()
        self.loginWindow.loginButton.clicked.connect(self.updateUser)
        self.showWindow.ShowFavoriteButton.clicked.connect(self.updateShowFavorite)
        self.movieWindow.MovieFavoriteButton.clicked.connect(self.updateMovieFavorite)
        self.searchWindow.pushButton.clicked.connect(self.updateSearchOptions)

        self.currentUserFavorites = []

        self.setEnabled(True)
        self.setFixedSize(800, 600)
        #self.setStyleSheet(u"QMainWindow {\n"
        #                         "background: linear-gradient(0.25turn, #3f87a6, #ebf8e1, #f69d3c);"
        #                         "}")

        
    
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")

        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 400)
        gradient.setColorAt(0.0, QColor(240, 240, 240))
        gradient.setColorAt(1.0, QColor(240, 160, 160))
        p.setBrush(QPalette.Window, QBrush(gradient))
        #self.centralwidget.setPalette(p)
        self.setPalette(p)

        self.MediaSearchButton = QPushButton(self.centralwidget, clicked=lambda: self.openSearchWindow())
        # self.MediaSearchButton = QPushButton(self.centralwidget, clicked=lambda: self.openSearchWindow())
        self.MediaSearchButton.setObjectName(u"MediaSearchButton")
        self.MediaSearchButton.setGeometry(QRect(320, 20, 101, 31))
        #self.MediaSearchButton.setStyleSheet("background-color: dimgray; border-radius: 5px; color: white; font-family: 'Kumbh Sans', sans-serif; font-weight: bold")
       
        
        

        #image label-contains user profile picture
        self.label = newLabel(self.centralwidget, u"label", (560, 120, 181, 181))
        self.label.setStyleSheet(u"QLabel {\n"
                                 "	background-image: url(Assets/ProfileImage.png)\n"
                                 "}")
        self.label.setPixmap(QPixmap(u"../../Assets/ProfileImage.jpg"))
        self.label.setScaledContents(True)

        #label contains username
        self.UserNameLabel = newLabel(self.centralwidget, u"UserNameLabel", (600, 300, 91, 20))

        #button to change user
        self.ChangeUserButton = QPushButton(self.centralwidget, clicked=lambda: self.openLoginWindow())
        # self.ChangeUserButton = QPushButton(self.centralwidget)
        self.ChangeUserButton.setObjectName(u"ChangeUserButton")
        self.ChangeUserButton.setGeometry(QRect(610, 320, 75, 24))

        self.label_2 = newLabel(self.centralwidget, u"label_2", (600, 360, 31, 16))

        self.AgeLabel = newLabel(self.centralwidget, u"AgeLabel", (630, 360, 49, 16))

        self.label_4 = newLabel(self.centralwidget, u"label_4", (20, 60, 51, 16))
        
        self.label_5 = newLabel(self.centralwidget, u"label_5", (580, 380, 51, 16))

        self.GenderLabel = newLabel(self.centralwidget, u"GenderLabel", (630, 380, 71, 16))

        self.label_3 = newLabel(self.centralwidget, u"label_3", (550, 400, 81, 16))
        
        self.NumFavsLabel = newLabel(self.centralwidget, u"NumFavsLabel", (630, 400, 51, 16))
    

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

        #self.menubar = QMenuBar(self)
        #self.menubar.setObjectName(u"menubar")
        #self.menubar.setGeometry(QRect(0, 0, 800, 22))
        #self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi(self)
        self.updateUser()

        QMetaObject.connectSlotsByName(self)

    def _createMenuBar(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        movieMenu = QMenu("&Movies", self)
        menuBar.addMenu(movieMenu)

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
        numFavs = psql.getNumFavs(self.currentUser)
        self.NumFavsLabel.setText(str(numFavs))
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

    

def newLabel(widget, name, geometry):
        print(type(geometry))
        label = QLabel(widget)
        label.setObjectName(name)
        label.setGeometry(QRect(geometry[0], geometry[1], geometry[2], geometry[3] ))
        #label.setStyleSheet(u"QLabel {\n"
        #                         "	color: white\n"
        #                         "}")
        return label