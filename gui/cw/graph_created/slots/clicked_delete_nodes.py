from PySide2.QtCore import Slot
from graph.graph_object_interface import GraphObjectInterface as GOI


@Slot()
def proc_clicked_delete_nodes(cwgc):
    nodes = split_text_into_nodes(cwgc.form_delete_nodes.text())
    GOI.delete_nodes(nodes)
    if not GOI.are_nodes_there():
        cwgc.image.setCurrentWidget(cwgc.label_empty_graph)
    else:
        render_path = GOI.get_render_image()
        cwgc.image_viewer.set_image(render_path)
    cwgc.form_delete_nodes.setText("")


def split_text_into_nodes(text):
    nodes = []
    if text != "":
        nodes = text.split()
    return nodes
