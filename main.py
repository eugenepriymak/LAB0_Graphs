from gui.main_window import MainWindow
from application.application import Application


if __name__ == "__main__":
    app = Application()
    main_window = MainWindow()
    main_window.show()
    app.exec_()
