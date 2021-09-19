from PySide2 import QtWidgets
from gui.cw.graph_not_created.cwgnc import CWGraphNotCreated
from gui.cw.graph_created.cwgc import CWGraphCreated
from gui.cw.search.cws import CWSearch


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        def init_title():
            self.setWindowTitle("Visualization of BFS, DFS")

        # "CW" stands for "Central Widget"
        def init_cw():
            self.cw_graph_not_created = CWGraphNotCreated(main_window=self)
            self.cw_graph_created = CWGraphCreated(main_window=self)
            self.cw_search = CWSearch(main_window=self)

            self.cw = QtWidgets.QStackedWidget()
            self.cw.addWidget(self.cw_graph_not_created)
            self.cw.addWidget(self.cw_graph_created)
            self.cw.addWidget(self.cw_search)
            self.set_cw_graph_not_created_current()
            self.setCentralWidget(self.cw)

        def init_status_bar():
            self.sb = QtWidgets.QStatusBar()
            self.setStatusBar(self.sb)

        super().__init__()
        init_cw()
        init_title()
        init_status_bar()

    def set_cw_graph_not_created_current(self):
        self.cw.setCurrentWidget(self.cw_graph_not_created)

    def set_cw_graph_created_current(self):
        self.cw.setCurrentWidget(self.cw_graph_created)

    def set_cw_search_current(self):
        self.cw.setCurrentWidget(self.cw_search)
