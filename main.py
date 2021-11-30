import sys
from PySide6.QtWidgets import (QApplication)
import backend.psql_handlers as psql
import image_download
from UI.WindowsFiles.UserHomePage import UserHomePage
qss = """

QPushButton {
    background-color: dimgray; 
    border-radius: 5px; 
    color: white; 
    font-family: 'Gotham Medium', sans-serif; 
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
                                      stop:0 #9198e5, stop:1 #282629);
}

#showWindow {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                      stop:0 #e66465, stop:1 #282629);
}

#movieWindow {
    background-color: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                      stop:0 #34DB61, stop:1 #282629);
}




QToolBar {
    background-color: dimgray;
}



QPushButton:hover {
    background-color: #9518fc;
}

QLabel {
    color: white;
    font-family: 'Gotham Medium', sans-serif;
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
