from PySide2.QtCore import Slot
from graph.graph_object_interface import GraphObjectInterface as GOI


@Slot()
def proc_clicked_start_bfs(cwgc):
    if not GOI.are_nodes_there():
        cwgc.form_start_bfs.setText("")
        cwgc.main_window.sb.showMessage("ERROR: there aren't nodes in the graph", 5000)
        return
    passed_nodes = split_text_into_nodes(cwgc.form_start_bfs.text())
    cwgc.form_start_bfs.setText("")
    if len(passed_nodes) == 0:
        cwgc.main_window.sb.showMessage("ERROR: the input is empty", 5000)
        return
    if len(passed_nodes) > 1:
        cwgc.main_window.sb.showMessage("ERROR: the input contains more than 1 node", 5000)
        return
    start_node = passed_nodes[0]
    if start_node not in GOI.get_nodes():
        cwgc.main_window.sb.showMessage(f"ERROR: there isn't a node with name {start_node}", 5000)
        return
    render_paths = GOI.get_bfs_render_images(start_node)
    cwgc.main_window.cw_search.set_render_paths(render_paths)
    cwgc.main_window.set_cw_search_current()


def split_text_into_nodes(text):
    nodes = []
    if text != "":
        nodes = text.split()
    return nodes
