from PySide2.QtCore import Slot
from graph.graph_object_interface import GraphObjectInterface as GOI
from gui.cw.graph_created.reader_add_from_file import Reader


@Slot()
def proc_clicked_add_from_file(cwgc):
    def get_encoding():
        encodings = {type(cwgc).ENCODING_ASCII: "ascii",
                     type(cwgc).ENCODING_UTF_8: "utf-8",
                     type(cwgc).ENCODING_UTF_16: "utf-16",
                     type(cwgc).ENCODING_UTF_32: "utf-32"}
        return encodings[cwgc.combo_box_add_from_file.currentText()]

    def get_path():
        path = cwgc.form_add_nodes_and_edges_from_file.text()
        if path == "" or path.isspace():
            return None
        else:
            return path.strip()

    def get_nodes_and_edges_from_file(path, encoding):
        with open(file=path, encoding=encoding, mode="rt") as file:
            reader = Reader(file, buff_size=128)
            nodes, edges = reader.read_file()
            return nodes, edges

    encoding = get_encoding()
    path = get_path()
    cwgc.form_add_nodes_and_edges_from_file.setText("")
    if path is None:
        return

    try:
        new_nodes, new_edges = get_nodes_and_edges_from_file(path, encoding)
    except FileNotFoundError:
        cwgc.main_window.sb.showMessage(f"ERROR: file {path} is not found", 5000)
        return
    except UnicodeError:
        cwgc.main_window.sb.showMessage(f"ERROR: file {path} has other encoding", 5000)
        return

    if not GOI.are_nodes_there():
        if new_nodes == [] and new_edges == []:
            return
        else:
            cwgc.image.setCurrentWidget(cwgc.image_viewer)
    GOI.add_nodes(new_nodes)
    GOI.add_edges(new_edges)
    render_path = GOI.get_render_image()
    cwgc.image_viewer.set_image(render_path)


def split_text_into_nodes(text):
    nodes = []
    if text != "":
        nodes = text.split()
    return nodes
