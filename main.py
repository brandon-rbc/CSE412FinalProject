import sys
from PySide6.QtWidgets import (QApplication)
import backend.psql_handlers as psql
import image_download
from UI.WindowsFiles.UserHomePage import UserHomePage
qss = """
QMenuBar {
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                      stop:0 lightgray, stop:1 darkgray);
}

QPushButton {
    background-color: dimgray; 
    border-radius: 5px; 
    color: white; 
    font-family: 'Kumbh Sans', sans-serif; 
    font-weight: bold
}

QPushButton:hover {
    background-color: #9518fc;
}

QScrollArea {
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
