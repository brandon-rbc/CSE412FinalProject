from PySide6 import QtCore
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QLineEdit, QTextEdit, QScrollArea
from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, Qt)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton, QStatusBar, QWidget, QMenu)


class SearchWindow(QMainWindow):
    def __init__(self, page):
        super().__init__()
        self.setFixedSize(803, 587)
        self.setObjectName("searchWindow")
        self.centralwidget = QWidget(self)
        self.homepage = page
        self._createMenuBar()
        #self.centralwidget.setStyleSheet("background-color: black;")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 70, 761, 451))
        self.gridLayoutWidget.setStyleSheet("background-color: black;")
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        #self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("background-color: black;")
        self.scrollArea.setGeometry(QRect(20, 70, 761, 451))
        self.scrollArea.setWidgetResizable(True)
        #self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
        


        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(320, 20, 451, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet("padding: 5px;")

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.textEdit = QLineEdit(self.horizontalLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.installEventFilter(self)

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
        #self.SortByBoxSearch.currentIndexChanged.connect(self.homepage.updateSearchOptions())
        self.SortByBoxSearch.currentIndexChanged.connect(self.homepage.updateSearchOptions)

        self.horizontalLayout.addWidget(self.SortByBoxSearch)

        self.setCentralWidget(self.centralwidget)


        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)
        # setupUi

    def _createMenuBar(self):
        menuBar = QMenuBar(self)
        self.setMenuBar(menuBar)
        movieMenu = QMenu("Media Search", self)
        menuBar.addMenu(movieMenu)

    def retranslateUi(self, SearchWindow):#qtdesigner generated code
        SearchWindow.setWindowTitle(QCoreApplication.translate("SearchWindow", u"FilmFriend", None))
        self.pushButton.setText(QCoreApplication.translate("SearchWindow", u"Search", None))
        self.label.setText(QCoreApplication.translate("SearchWindow", u"Search By:", None))
        self.SortByBoxSearch_2.setItemText(0, QCoreApplication.translate("SearchWindow", u"Title", None))
        self.SortByBoxSearch_2.setItemText(1, QCoreApplication.translate("SearchWindow", u"Director", None))
        self.SortByBoxSearch_2.setItemText(2, QCoreApplication.translate("SearchWindow", u"Genre", None))

        self.label_6.setText(QCoreApplication.translate("SearchWindow", u"Sort By:", None))
        self.SortByBoxSearch.setItemText(0, QCoreApplication.translate("SearchWindow", u"Rating", None))
        self.SortByBoxSearch.setItemText(1, QCoreApplication.translate("SearchWindow", u"A-Z", None))

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress and obj is self.textEdit:
            if event.key() == QtCore.Qt.Key_Return and self.textEdit.hasFocus():
                self.homepage.updateSearchOptions()
                self.textEdit.clear()
        return super().eventFilter(obj, event)