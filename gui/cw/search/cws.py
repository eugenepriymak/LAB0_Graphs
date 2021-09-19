from PySide2 import QtWidgets
from functools import partial
from gui.image_viewer import ImageViewer
from gui.cw.search.slots.clicked_exit_search import proc_clicked_exit_search
from gui.cw.search.slots.clicked_prev_node import proc_clicked_prev_node
from gui.cw.search.slots.clicked_next_node import proc_clicked_next_node


class CWSearch(QtWidgets.QWidget):
    def __init__(self, main_window):
        def init_layout():
            self.base_layout = QtWidgets.QHBoxLayout()
            init_images_part()
            init_input_part()
            self.setLayout(self.base_layout)

        def init_images_part():
            self.image_viewer = ImageViewer()
            self.base_layout.addWidget(self.image_viewer)

        def init_input_part():
            self.input_layout = QtWidgets.QVBoxLayout()
            init_previous_node_and_next_node()
            init_exit_search()
            self.base_layout.addLayout(self.input_layout)

        def init_previous_node_and_next_node():
            layout = QtWidgets.QHBoxLayout()
            self.button_prev_node = QtWidgets.QPushButton("Previous node")
            self.button_prev_node.hide()
            self.button_prev_node.clicked.connect(partial(proc_clicked_prev_node, self))
            layout.addWidget(self.button_prev_node)

            self.button_next_node = QtWidgets.QPushButton("Next node")
            self.button_next_node.hide()
            self.button_next_node.clicked.connect(partial(proc_clicked_next_node, self))
            layout.addWidget(self.button_next_node)

            self.input_layout.addLayout(layout)

        def init_exit_search():
            self.button_exit_search = QtWidgets.QPushButton("Exit search")
            self.button_exit_search.clicked.connect(partial(proc_clicked_exit_search, self))
            self.input_layout.addWidget(self.button_exit_search)

        super().__init__()
        self.main_window = main_window
        self.curr_render_ind = None
        self.render_paths = []
        init_layout()

    def set_render_paths(self, paths):
        processed_paths = []
        for path in paths:
            if path != "" and not path.isspace():
                processed_paths.append(path.strip())
        assert processed_paths != []

        self.render_paths = processed_paths
        self.curr_render_ind = 0
        self.main_window.cw_search.image_viewer.set_image(self.render_paths[self.curr_render_ind])
        if len(self.render_paths) > 1:
            self.button_next_node.show()

    def clear_render_paths(self):
        self.curr_render_ind = None
        self.render_paths = []
        self.button_prev_node.hide()
        self.button_next_node.hide()

    def set_next_render_current(self):
        assert self.curr_render_ind is not None
        assert self.render_paths != []
        assert self.curr_render_ind < len(self.render_paths) - 1

        first_render_ind = 0
        last_render_ind = len(self.render_paths) - 1
        if self.curr_render_ind == first_render_ind:
            self.button_prev_node.show()
        if self.curr_render_ind == last_render_ind - 1:
            self.button_next_node.hide()
        self.curr_render_ind += 1
        self.main_window.cw_search.image_viewer.set_image(self.render_paths[self.curr_render_ind])

    def set_prev_render_current(self):
        assert self.curr_render_ind is not None
        assert self.render_paths != []
        assert self.curr_render_ind > 0

        first_render_ind = 0
        last_render_ind = len(self.render_paths) - 1
        if self.curr_render_ind == first_render_ind + 1:
            self.button_prev_node.hide()
        if self.curr_render_ind == last_render_ind:
            self.button_next_node.show()
        self.curr_render_ind -= 1
        self.main_window.cw_search.image_viewer.set_image(self.render_paths[self.curr_render_ind])
