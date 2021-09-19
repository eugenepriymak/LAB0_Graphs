from PySide2.QtCore import Slot


@Slot()
def proc_clicked_prev_node(cws):
    cws.set_prev_render_current()
