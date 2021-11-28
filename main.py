import sys
from PySide6.QtWidgets import (QApplication)
import backend.psql_handlers as psql
import image_download
from UI.WindowsFiles.UserHomePage import UserHomePage

if __name__ == "__main__":
    psql.main()
    image_download.downloadImages()
    app = QApplication(sys.argv)
    userWindow = UserHomePage()
    userWindow.show()
    sys.exit((app.exec()))
