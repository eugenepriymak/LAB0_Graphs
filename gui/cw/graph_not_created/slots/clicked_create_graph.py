from PySide2.QtCore import Slot
from graph.graph_object_interface import GraphObjectInterface as GOI


@Slot()
def proc_clicked_create_graph(cwgnc):
    if cwgnc.button_is_directed.isChecked():
        GOI.create(is_directed=True)
    else:
        GOI.create(is_directed=False)
    cwgnc.main_window.set_cw_graph_created_current()
