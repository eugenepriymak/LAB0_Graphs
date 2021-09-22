from PySide2.QtCore import Slot


@Slot()
def proc_clicked_exit_search(cws):
    cws.clear_render_paths()
    cws.main_window.set_cw_graph_created_current()
