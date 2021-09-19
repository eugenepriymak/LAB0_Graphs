from PySide2.QtCore import Slot
from graph.graph_object_interface import GraphObjectInterface as GOI


@Slot()
def proc_clicked_add_nodes(cwgc):
    new_nodes = split_text_into_nodes(cwgc.form_add_nodes.text())
    if not GOI.are_nodes_there():
        if new_nodes == []:
            cwgc.form_add_nodes.setText("")
            return
        else:
            cwgc.image.setCurrentWidget(cwgc.image_viewer)
    GOI.add_nodes(new_nodes)
    render_path = GOI.get_render_image()
    cwgc.image_viewer.set_image(render_path)
    cwgc.form_add_nodes.setText("")


def split_text_into_nodes(text):
    nodes = []
    if text != "":
        nodes = text.split()
    return nodes
