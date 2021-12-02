import sys
from PySide6.QtWidgets import (QApplication)
import backend.psql_handlers as psql
import image_download
from UI.WindowsFiles.UserHomePage import UserHomePage
# CSS code for display functionality
qss = """

QPushButton {
    background-color: #404040; 
    border-radius: 5px; 
    color: white; 
    font-family: 'Trebuchet MS, sans-serif; 
    font-weight: bold;
}

QScrollArea {
    background-color: black;
}

QMenuBar {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                      stop:0 lightgray, stop:1 darkgray);
}

QMainWindow {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                      stop:0 #eb3434, stop:1 #282629);
}

#showWindow {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                      stop:0 indianred, stop:1 #282629);
}

#movieWindow {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                      stop:0 darksalmon, stop:1 #282629);
}

#searchWindow {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                      stop:0 #db630d, stop:1 #282629);
}

#loginWindow {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                      stop:0 #e07919, stop:1 #282629);
}


#mediaButton:hover {
    color: black;

}


QPushButton:hover {
    background-color: darkgray;
    color:black;
}


QLabel {
    color: white;
    font-family: 'Trebuchet MS', sans-serif;
}

#searchCentralWidget {
    background-color: black;
}
"""
if __name__ == "__main__":
    psql.main()
    image_download.downloadImages()
    app = QApplication(sys.argv)
    app.setStyleSheet(qss)
    userWindow = UserHomePage()
    userWindow.show()
    sys.exit((app.exec()))
