from PySide2 import QtWidgets
from gui.image_viewer import ImageViewer
from functools import partial
from gui.cw.graph_created.slots.clicked_add_nodes import proc_clicked_add_nodes
from gui.cw.graph_created.slots.clicked_add_edges import proc_clicked_add_edges
from gui.cw.graph_created.slots.clicked_delete_nodes import proc_clicked_delete_nodes
from gui.cw.graph_created.slots.clicked_delete_edges import proc_clicked_delete_edges
from gui.cw.graph_created.slots.clicked_add_from_file import proc_clicked_add_from_file
from gui.cw.graph_created.slots.clicked_start_bfs import proc_clicked_start_bfs
from gui.cw.graph_created.slots.clicked_start_dfs import proc_clicked_start_dfs
from gui.cw.graph_created.slots.clicked_delete_graph import proc_clicked_delete_graph


class CWGraphCreated(QtWidgets.QWidget):
    ENCODING_UTF_8 = "UTF-8"
    ENCODING_UTF_16 = "UTF-16"
    ENCODING_UTF_32 = "UTF-32"
    ENCODING_ASCII = "ASCII"

    def __init__(self, main_window):
        def init_cw_layout():
            self.base_layout = QtWidgets.QHBoxLayout()
            init_image_part()
            init_input_part()
            self.setLayout(self.base_layout)

        def init_image_part():
            self.label_empty_graph = QtWidgets.QLabel("Graph is empty")
            self.image_viewer = ImageViewer()
            self.image = QtWidgets.QStackedWidget()
            self.image.addWidget(self.label_empty_graph)
            self.image.addWidget(self.image_viewer)
            self.image.setCurrentWidget(self.label_empty_graph)
            self.base_layout.addWidget(self.image)

        def init_input_part():
            self.input_layout = QtWidgets.QVBoxLayout()
            init_add_nodes()
            init_delete_nodes()
            init_add_edges()
            init_delete_edges()
            init_add_from_file()
            init_start_dfs()
            init_start_bfs()
            init_delete_graph()
            self.base_layout.addLayout(self.input_layout)

        def init_add_nodes():
            layout = QtWidgets.QHBoxLayout()
            self.button_add_nodes = QtWidgets.QPushButton("Add nodes")
            self.button_add_nodes.clicked.connect(partial(proc_clicked_add_nodes, self))
            self.form_add_nodes = QtWidgets.QLineEdit()
            layout.addWidget(self.button_add_nodes)
            layout.addWidget(self.form_add_nodes)
            self.input_layout.addLayout(layout)

        def init_delete_nodes():
            layout = QtWidgets.QHBoxLayout()
            self.button_delete_nodes = QtWidgets.QPushButton("Delete nodes")
            self.button_delete_nodes.clicked.connect(partial(proc_clicked_delete_nodes, self))
            self.form_delete_nodes = QtWidgets.QLineEdit()
            layout.addWidget(self.button_delete_nodes)
            layout.addWidget(self.form_delete_nodes)
            self.input_layout.addLayout(layout)

        def init_add_edges():
            layout = QtWidgets.QHBoxLayout()
            self.button_add_edges = QtWidgets.QPushButton("Add edges")
            self.button_add_edges.clicked.connect(partial(proc_clicked_add_edges, self))
            self.form_add_edges = QtWidgets.QLineEdit()
            layout.addWidget(self.button_add_edges)
            layout.addWidget(self.form_add_edges)
            self.input_layout.addLayout(layout)

        def init_delete_edges():
            layout = QtWidgets.QHBoxLayout()
            self.button_delete_edges = QtWidgets.QPushButton("Delete edges")
            self.button_delete_edges.clicked.connect(partial(proc_clicked_delete_edges, self))
            self.form_delete_edges = QtWidgets.QLineEdit()
            layout.addWidget(self.button_delete_edges)
            layout.addWidget(self.form_delete_edges)
            self.input_layout.addLayout(layout)

        def init_add_from_file():
            layout = QtWidgets.QHBoxLayout()
            self.button_add_from_file = QtWidgets.QPushButton("Add nodes and edges from file")
            self.button_add_from_file.clicked.connect(partial(proc_clicked_add_from_file, self))
            self.combo_box_add_from_file = QtWidgets.QComboBox()
            self.combo_box_add_from_file.addItems([CWGraphCreated.ENCODING_UTF_8,
                                                   CWGraphCreated.ENCODING_UTF_16,
                                                   CWGraphCreated.ENCODING_UTF_32,
                                                   CWGraphCreated.ENCODING_ASCII])
            self.form_add_nodes_and_edges_from_file = QtWidgets.QLineEdit()
            layout.addWidget(self.button_add_from_file)
            layout.addWidget(self.combo_box_add_from_file)
            layout.addWidget(self.form_add_nodes_and_edges_from_file)
            self.input_layout.addLayout(layout)

        def init_start_dfs():
            layout = QtWidgets.QHBoxLayout()
            self.button_start_dfs = QtWidgets.QPushButton("Start DFS from node")
            self.button_start_dfs.clicked.connect(partial(proc_clicked_start_dfs, self))
            self.form_start_dfs = QtWidgets.QLineEdit()
            layout.addWidget(self.button_start_dfs)
            layout.addWidget(self.form_start_dfs)
            self.input_layout.addLayout(layout)

        def init_start_bfs():
            layout = QtWidgets.QHBoxLayout()
            self.button_start_bfs = QtWidgets.QPushButton("Start BFS from node")
            self.button_start_bfs.clicked.connect(partial(proc_clicked_start_bfs, self))
            self.form_start_bfs = QtWidgets.QLineEdit()
            layout.addWidget(self.button_start_bfs)
            layout.addWidget(self.form_start_bfs)
            self.input_layout.addLayout(layout)

        def init_delete_graph():
            self.button_delete_graph = QtWidgets.QPushButton("Delete graph")
            self.button_delete_graph.clicked.connect(partial(proc_clicked_delete_graph, self))
            self.input_layout.addWidget(self.button_delete_graph)

        super().__init__()
        self.main_window = main_window
        init_cw_layout()

    def set_label_empty_graph_current(self):
        self.image.setCurrentWidget(self.label_empty_graph)

    def set_image_viewer_current(self):
        self.image.setCurrentWidget(self.image_viewer)
