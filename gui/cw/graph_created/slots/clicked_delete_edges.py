from PySide2.QtCore import Slot
from graph.graph_object_interface import GraphObjectInterface as GOI


@Slot()
def proc_clicked_delete_edges(cwgc):
    edges = split_text_into_edges(cwgc.form_delete_edges.text())
    GOI.delete_edges(edges)
    render_path = GOI.get_render_image()
    cwgc.image_viewer.set_image(render_path)
    cwgc.form_delete_edges.setText("")


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
