from PySide2.QtCore import Slot
from graph.graph_object_interface import GraphObjectInterface as GOI


@Slot()
def proc_clicked_delete_graph(cwgc):
    GOI.delete()
    cwgc.set_label_empty_graph_current()
    cwgc.image_viewer.clear_image()
    cwgc.main_window.set_cw_graph_not_created_current()
