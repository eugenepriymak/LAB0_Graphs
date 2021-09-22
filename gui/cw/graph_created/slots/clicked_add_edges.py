from PySide2.QtCore import Slot
from graph.graph_object_interface import GraphObjectInterface as GOI


@Slot()
def proc_clicked_add_edges(cwgc):
    new_edges = split_text_into_edges(cwgc.form_add_edges.text())
    if not GOI.are_nodes_there():
        if new_edges == []:
            cwgc.form_add_edges.setText("")
            return
        else:
            cwgc.image.setCurrentWidget(cwgc.image_viewer)
    GOI.add_edges(new_edges)
    render_path = GOI.get_render_image()
    cwgc.image_viewer.set_image(render_path)
    cwgc.form_add_edges.setText("")


def split_text_into_edges(text):
    edges = []
    if text == "":
        return edges
    nodes = text.split()
    node_ind = 0
    while node_ind < len(nodes) - 2:
        edge = (nodes[node_ind], nodes[node_ind + 1])
        edges.append(edge)
        node_ind += 2
    if len(nodes) % 2 == 0:
        last_edge = (nodes[node_ind], nodes[node_ind + 1])
        edges.append(last_edge)
    return edges
