from PySide6.QtWidgets import QMenu, QScrollArea
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtGui import (QPixmap, QFont, QPainter, QBrush, QPen, QLinearGradient, QPalette, QColor, QAction, QIcon)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton, QStatusBar, QWidget, QToolBar, QVBoxLayout)

import backend.psql_handlers as psql
from UI.WindowsFiles.SearchWindow import SearchWindow
from UI.WindowsFiles.LoginWindow import LoginWindow
from UI.WindowsFiles.MovieWindow import MovieWindow
from UI.WindowsFiles.ShowWindow import ShowWindow
#from UI.WindowsFiles.ProfileWindow import ProfileWindow

windowWidth = 800
windowHeight = 600
class UserHomePage(QMainWindow):
    #initializes all elements of UserHomePage including UI
    def __init__(self):
        super().__init__()
        
        self.setObjectName(u"userHomePage")
        self.setFixedSize(windowWidth, windowHeight)
        self.currentUser = -1
        self.initializeChildWindows()
        self.initializeUI()
        self.retranslateUi(self)
        self.updateUser()

        QMetaObject.connectSlotsByName(self)
        
    def initializeChildWindows(self):
        self.loginWindow = LoginWindow()
        self.searchWindow = SearchWindow(self)
        self.showWindow = ShowWindow()
        self.movieWindow = MovieWindow()

    def initializeUI(self):
        self.loginWindow.loginButton.clicked.connect(self.updateUser)
        self.showWindow.ShowFavoriteButton.clicked.connect(self.updateShowFavorite)
        self.movieWindow.MovieFavoriteButton.clicked.connect(self.updateMovieFavorite)
        self.searchWindow.pushButton.clicked.connect(self.updateSearchOptions)
        
        self._createMenuBar()
        self.UserBackground = QLabel(self)
        self.UserBackground.setGeometry(((3/4)*windowWidth) - 100, 150, 200, 300)
        self.UserBackground.setObjectName(u"UserBackground")
        self.UserBackground.setStyleSheet("background: rgba(160, 160, 160, 0.50); border-radius: 3px;")

        self.currentUserFavorites = []

        self.setEnabled(True)
        
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")

        self.UserImage = newLabel(self.centralwidget, u"UserImage", (((3/4)*windowWidth) - 90, 120, 180, 180))
        self.UserImage.setStyleSheet(u"QLabel {\n"
                                 "	background-image: url(Assets/ProfileImage.png);\n"
                                 "  width: 180px;"
                                 "  height: 180px"
                                 "}")

        self.UserImage.setScaledContents(True)

        self.ChangeUserButton = QPushButton(self.centralwidget, clicked=lambda: self.openLoginWindow())
        self.ChangeUserButton.setObjectName(u"ChangeUserButton")
        self.ChangeUserButton.setGeometry(QRect((3 / 4) * windowWidth-37, 390, 75, 24)) #centering button
    
        self.UserNameLabel = newLabel(self.centralwidget, u"UserNameLabel", (((3/4)*windowWidth) - 45, 300, 90, 20))
        self.UserNameLabel.setAlignment(Qt.AlignCenter)#align username center
        self.ageTitleLabel = newLabel(self.centralwidget, u"ageTitleLabel", (((3/4)*windowWidth) - 70, 320, 31, 16))
        self.ageTitleLabel.setAlignment(Qt.AlignLeft)
        self.AgeLabel = newLabel(self.centralwidget, u"AgeLabel", (645, 320, 49, 16))
        self.FavTitleLabel = newLabel(self.centralwidget, u"FavTitleLabel", (20, 60, 51, 16))
        self.GenderTitleLabel = newLabel(self.centralwidget, u"GenderTitleLabel", (((3/4)*windowWidth) - 70, 340, 51, 16))
        self.GenderLabel = newLabel(self.centralwidget, u"GenderLabel", (645, 340, 71, 16))
        self.NumFavTitleLabel = newLabel(self.centralwidget, u"NumFavTitleLabel", (((3/4)*windowWidth) - 70, 360, 81, 16))
        self.NumFavsLabel = newLabel(self.centralwidget, u"NumFavsLabel", (645, 360, 51, 16))

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 80, 400, 451))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setDefaultPositioning(2, Qt.Orientation.Horizontal)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("background-color: black;")
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(15, 80, 370, 451))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 10, 108, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.SortByTitleLabel = QLabel(self.horizontalLayoutWidget)
        self.SortByTitleLabel.setObjectName(u"SortByTitleLabel")
        self.SortByTitleLabel.setEnabled(True)

        self.horizontalLayout.addWidget(self.SortByTitleLabel)

        self.SortByBox = QComboBox(self.horizontalLayoutWidget)
        self.SortByBox.addItem("")
        self.SortByBox.addItem("")
        self.SortByBox.setObjectName(u"SortByBox")
        self.SortByBox.currentIndexChanged.connect(self.updateUser)

        self.horizontalLayout.addWidget(self.SortByBox)

        self.MediaSearchButton = QPushButton(self.centralwidget, clicked=lambda: self.openSearchWindow())
        self.MediaSearchButton.setObjectName(u"MediaSearchButton")
        self.MediaSearchButton.setGeometry(QRect(((1/4)*windowWidth) - 50, 10, 100, 41))

        self.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

    #adds menu bar to window
    def _createMenuBar(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        movieMenu = QMenu("User Homepage", self)
        menuBar.addMenu(movieMenu)

    #qtdesigner generated code
    def retranslateUi(self, UserHomePage):
        UserHomePage.setWindowTitle(QCoreApplication.translate("UserHomePage", u"FilmFriend", None))
        self.MediaSearchButton.setText(QCoreApplication.translate("UserHomePage", u"Search Media", None))
        self.UserImage.setText("")
        self.UserNameLabel.setText(QCoreApplication.translate("UserHomePage", u"USERNAME HERE", None))
        self.ChangeUserButton.setText(QCoreApplication.translate("UserHomePage", u"Not You?", None))
        self.ageTitleLabel.setText(QCoreApplication.translate("UserHomePage", u"Age: ", None))
        self.AgeLabel.setText(QCoreApplication.translate("UserHomePage", u"AgeLabel", None))
        self.FavTitleLabel.setText(QCoreApplication.translate("UserHomePage", u"Favorites", None))
        self.GenderTitleLabel.setText(QCoreApplication.translate("UserHomePage", u"Gender:", None))
        self.GenderLabel.setText(QCoreApplication.translate("UserHomePage", u"GenderLabel", None))
        self.NumFavTitleLabel.setText(QCoreApplication.translate("UserHomePage", u"# of Favorites:", None))
        self.NumFavsLabel.setText(QCoreApplication.translate("UserHomePage", u"NumFavs", None))
        self.SortByTitleLabel.setText(QCoreApplication.translate("UserHomePage", u"Sort By:", None))
        self.SortByBox.setItemText(0, QCoreApplication.translate("UserHomePage", u"Rating", None))
        self.SortByBox.setItemText(1, QCoreApplication.translate("UserHomePage", u"A-Z", None))

    #displays login window
    def openLoginWindow(self):
        self.loginWindow.show()

    #displays search window
    def openSearchWindow(self):
        self.updateSearchOptions()
        self.searchWindow.show()

    #fetches show info from database and passes into new show window
    def openShowWindow(self):
        button = self.sender()
        name = button.text()
        self.showWindow.setWindowTitle(name)
        self.showWindow.ShowTitleLabel.setText(f'Title: {name}')
        mediaID = psql.getMediaID(name)
        self.showWindow.mediaID = mediaID
        
        #checks if show is in favorites. changes button accordingly
        if psql.checkInFavorites(self.currentUser, mediaID):
            self.showWindow.ShowFavoriteButton.setText('Remove from Favorites')
        else:
            self.showWindow.ShowFavoriteButton.setText('Add to Favorites')
        
        #passes show data into labels
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
        rating_string = f'IMDb rating: {rating}'
        self.showWindow.ShowRatingLabel.setText(rating_string)
        self.showWindow.ShowNumSeasonsLabel.setText(season_string)
        self.showWindow.ShowNumEpisodesLabel.setText(episode_string)
        self.showWindow.ShowImageLabel.setPixmap(QPixmap(f'image_holder/{id}'))
        self.showWindow.ShowImageLabel.setScaledContents(True)
        self.showWindow.show()

    #fetches show info from database and passes into new show window
    def openMovieWindow(self):
        button = self.sender()
        name = button.text()
        self.movieWindow.setWindowTitle(name)
        self.movieWindow.MovieTitleLabel.setText(f'Title: {name}')
        mediaID = psql.getMediaID(name)
        self.movieWindow.mediaID = mediaID

        #checks if movie is in favorites. changes button accordingly
        if psql.checkInFavorites(self.currentUser, mediaID):
            self.movieWindow.MovieFavoriteButton.setText('Remove from Favorites')
        else:
            self.movieWindow.MovieFavoriteButton.setText('Add to Favorites')

        #passes movie data into labels
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
        rating_string = f'IMDb rating: {rating}'
        self.movieWindow.MovieRatingLabel.setText(rating_string)
        self.movieWindow.MovieImageLabel.setPixmap(QPixmap(f'image_holder/{id}'))
        self.movieWindow.MovieImageLabel.setScaledContents(True)
        self.movieWindow.show()

    #updates favorite button after adding/removing from user favorites
    def updateMovieFavorite(self):
        sender = self.sender()
        if sender.text() == 'Add to Favorites':
            psql.addFavorite(self.currentUser, self.movieWindow.mediaID)
            self.movieWindow.MovieFavoriteButton.setText('Remove from Favorites')
        elif sender.text() == 'Remove from Favorites':
            psql.removeFavorite(self.currentUser, self.movieWindow.mediaID)
            self.movieWindow.MovieFavoriteButton.setText('Add to Favorites')
        self.updateUser()

    #updates favorite button after adding/removing from user favorites
    def updateShowFavorite(self):
        sender = self.sender()
        if sender.text() == 'Add to Favorites':
            psql.addFavorite(self.currentUser, self.showWindow.mediaID)
            self.showWindow.ShowFavoriteButton.setText('Remove from Favorites')
        elif sender.text() == 'Remove from Favorites':
            psql.removeFavorite(self.currentUser, self.showWindow.mediaID)
            self.showWindow.ShowFavoriteButton.setText('Add to Favorites')
        self.updateUser()

    #updates user information and favorites
    def updateUser(self):
        #updates labels
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

        #clear gridlayout
        num_delete = self.gridLayout.columnCount() * self.gridLayout.rowCount()
        for i in range(num_delete):
            if self.gridLayout.itemAt(i):
                self.gridLayout.itemAt(i).widget().deleteLater()

        #finds user favorites and displays them in scroll area
        numFavs = psql.getNumFavs(self.currentUser)
        if numFavs > 0:
            for favorite in self.currentUserFavorites:
                media_image = QLabel(self.centralwidget)
                media_image.setObjectName(u"label")
                media_image.setFixedSize(190, 260)
                media_image.setPixmap(QPixmap(f'image_holder/{favorite[1]}'))
                media_image.setScaledContents(True)
                if favorite[3] == 'show':
                    self.media_button = QPushButton(favorite[2])

                    self.media_button.setGeometry(QRect(320, 20, 101, 31))
                    self.media_button.clicked.connect(self.openShowWindow)
                    self.media_button.setStyleSheet("background: indianred")
                else:
                    self.media_button = QPushButton(favorite[2])
                    self.media_button.clicked.connect(self.openMovieWindow)
                    self.media_button.setStyleSheet("background: darksalmon")
                    self.media_button.setText(favorite[2])
                

                self.gridLayout.addWidget(media_image)
                self.gridLayout.addWidget(self.media_button)

        #displays message when user has no favorites
        else:
            no_favs_label = QLabel(self.centralwidget)
            no_favs_label.setGeometry(QRect(320, 20, 101, 31))
            no_favs_label.setText('Click "Search Media" to find your favorite movies and shows!')
            no_favs_label.setStyleSheet("font-size: 13px;")
            no_favs_label.setAlignment(Qt.AlignCenter)
            self.gridLayout.addWidget(no_favs_label)
            self.gridLayout.addWidget(no_favs_label)
            
        self.NumFavsLabel.setText(str(numFavs))
        widget = QWidget()
        widget.setLayout(self.gridLayout)
        self.scrollArea.setWidget(widget)

    #references backend to perform search and updates scroll area in search page with results
    def updateSearchOptions(self):
        sort_method = self.searchWindow.SortByBoxSearch.currentText()
        search_method = self.searchWindow.SortByBoxSearch_2.currentText()
        search_query = self.searchWindow.textEdit.text()
        media = psql.getSearchMedia(sort_method, search_method, search_query)

        self.searchWindow.gridLayoutWidget = QWidget(self.centralwidget)
        self.searchWindow.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.searchWindow.gridLayoutWidget.setGeometry(QRect(20, 70, 761, 451))
        self.searchWindow.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.searchWindow.gridLayout.setObjectName(u"gridLayout")
        self.searchWindow.gridLayout.setContentsMargins(0, 0, 0, 0)

        widget = QWidget()
        widget.setLayout(self.searchWindow.gridLayout)
        self.searchWindow.scrollArea.setWidget(widget)

        #finds all media resulting from search and adds image to scroll area
        numMedia = len(media)
        if numMedia > 0:
            for item in media:
                media_image = QLabel(self.centralwidget)
                media_image.setObjectName(u"label")
                media_image.setFixedSize(200, 260)
                media_image.setPixmap(QPixmap(f'image_holder/{item[2]}'))
                media_image.setScaledContents(True)
                if item[4] == 'show':
                    media_button = QPushButton(item[0])
                    media_button.clicked.connect(self.openShowWindow)
                    media_button.setStyleSheet("background: indianred")
                else:
                    media_button = QPushButton(item[0])
                    media_button.clicked.connect(self.openMovieWindow)
                    media_button.setStyleSheet("background: darksalmon")
                media_button.setText(item[0])
                

                self.searchWindow.gridLayout.addWidget(media_image)
                self.searchWindow.gridLayout.addWidget(media_button)

        #displays message if no search results are found
        else:
            noResultsLabel = newLabel(self.centralwidget, "noResultsLabel", (320, 20, 700, 31))
            noResultsLabel.setText('No movies/shows could be found with the ' + search_method.lower() + ': ' + search_query)
            noResultsLabel.setStyleSheet("font-size: 13px;")
            noResultsLabel.setAlignment(Qt.AlignCenter)
    
            self.searchWindow.gridLayout.addWidget(noResultsLabel)
            self.searchWindow.gridLayout.addWidget(noResultsLabel)

        widget = QWidget()
        widget.setLayout(self.searchWindow.gridLayout)
        self.searchWindow.scrollArea.setWidget(widget)

    #quits application if home page is closed
    def closeEvent(self, event):
        quit()

#helper method for creating labels  
def newLabel(widget, name, geometry):
        label = QLabel(widget)
        label.setObjectName(name)
        label.setGeometry(QRect(geometry[0], geometry[1], geometry[2], geometry[3] ))
        return label