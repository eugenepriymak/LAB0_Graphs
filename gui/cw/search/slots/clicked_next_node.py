from PySide2.QtCore import Slot


@Slot()
def proc_clicked_next_node(cws):
    cws.set_next_render_current()
