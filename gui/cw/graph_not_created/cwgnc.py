from PySide2 import QtWidgets
from functools import partial
from gui.cw.graph_not_created.slots.clicked_create_graph import proc_clicked_create_graph


class CWGraphNotCreated(QtWidgets.QWidget):
    def __init__(self, main_window):
        def init_layout():
            self.base_layout = QtWidgets.QVBoxLayout()
            init_is_directed()
            init_create_a_graph()
            self.setLayout(self.base_layout)

        def init_is_directed():
            self.button_is_directed = QtWidgets.QCheckBox("Is directed")
            self.base_layout.addWidget(self.button_is_directed)

        def init_create_a_graph():
            self.button_create_a_graph = QtWidgets.QPushButton("Create a graph")
            self.button_create_a_graph.clicked.connect(partial(proc_clicked_create_graph, self))
            self.base_layout.addWidget(self.button_create_a_graph)

        super().__init__()
        self.main_window = main_window
        init_layout()
