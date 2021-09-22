from graph.graph_class import Graph
import graphviz


class GraphObjectInterface:
    # TODO: is it necessary to define empty __init__?

    @staticmethod
    def is_created():
        return is_graph_class_object_created() and is_graphviz_object_created()

    @staticmethod
    def create(is_directed):
        create_graph_class_object(is_directed)
        create_graphviz_object(is_directed)

    @staticmethod
    def delete():
        delete_graph_class_object()
        delete_graphviz_object()

    @staticmethod
    def are_nodes_there():
        if not GraphObjectInterface.is_created():
            return None
        return graph_class_object.nodes != []

    @staticmethod
    def add_nodes(nodes):
        if not GraphObjectInterface.is_created():
            return
        for node in nodes:
            graph_class_object.add_node(node)
            graphviz_object.node(node, style="filled", color=color_node_border, fillcolor=color_node_default)

    @staticmethod
    def add_edges(edges):
        if not GraphObjectInterface.is_created():
            return
        for edge in edges:
            graph_class_object.add_edge(edge[0], edge[1])
            graphviz_object.node(edge[0], style="filled", color=color_node_border, fillcolor=color_node_default)
            graphviz_object.node(edge[1], style="filled", color=color_node_border, fillcolor=color_node_default)
            graphviz_object.edge(edge[0], edge[1])

    @staticmethod
    def delete_nodes(nodes):
        if not GraphObjectInterface.is_created():
            return
        for node in nodes:
            graph_class_object.delete_node(node)
        rebuild_graphviz_object_by_graph_class_object()

    @staticmethod
    def delete_edges(edges):
        if not GraphObjectInterface.is_created():
            return
        for edge in edges:
            graph_class_object.delete_edge(edge[0], edge[1])
        rebuild_graphviz_object_by_graph_class_object()

    @staticmethod
    def get_nodes():
        if not GraphObjectInterface.is_created():
            return None
        nodes = []
        for node in graph_class_object.nodes:
            nodes.append(node)
        return nodes

    @staticmethod
    def get_render_image():
        if not GraphObjectInterface.is_created():
            return
        render_path = "resources/graph"
        render_format = "png"
        graphviz_object.render(render_path, format=render_format)
        return render_path + "." + render_format

    @staticmethod
    def get_dfs_render_images(start_node):
        if not GraphObjectInterface.is_created():
            return None
        if start_node not in graph_class_object.nodes:
            return None

        render_paths, render_path_base, render_format = [], "resources/DFS", "png"
        visits_counter = 1

        def visit_node(visited):
            nonlocal visits_counter
            graphviz_object_copy = set_non_default_colors_to_nodes(visited, [color_node_visited] * len(visited))
            render_path = render_path_base + str(visits_counter)
            render_paths.append(render_path + "." + render_format)
            graphviz_object_copy.render(render_path, format=render_format)
            visits_counter += 1

        visited = []
        stack = [start_node]
        while stack != []:
            node = stack.pop()
            visited.append(node)
            visit_node(visited)
            for outgoing in graph_class_object.get_outgoing_nodes(node):
                if outgoing not in visited and outgoing not in stack:
                    stack.append(outgoing)

        return render_paths

    @staticmethod
    def get_bfs_render_images(start_node):
        if not GraphObjectInterface.is_created():
            return None
        if start_node not in graph_class_object.nodes:
            return None

        render_paths, render_path_base, render_format = [], "resources/BFS", "png"
        visits_counter = 1

        def visit_node(visited):
            nonlocal visits_counter
            graphviz_object_copy = set_non_default_colors_to_nodes(visited, [color_node_visited] * len(visited))
            render_path = render_path_base + str(visits_counter)
            render_paths.append(render_path + "." + render_format)
            graphviz_object_copy.render(render_path, format=render_format)
            visits_counter += 1

        visited = []
        queue = [start_node]
        while queue != []:
            node = queue.pop(0)
            visited.append(node)
            visit_node(visited)
            for outgoing in graph_class_object.get_outgoing_nodes(node):
                if outgoing not in visited and outgoing not in queue:
                    queue.append(outgoing)

        return render_paths


graph_class_object = None
graphviz_object = None

color_node_border = "black"
color_node_default = "white"
color_node_visited = "red"


def create_graph_class_object(is_directed):
    global graph_class_object
    graph_class_object = Graph(is_directed)


def create_graphviz_object(is_directed):
    global graphviz_object
    graphviz_object = graphviz.Digraph(strict=True) if is_directed else graphviz.Graph(strict=True)
    graphviz_object.attr("node", color=color_node_default)


def is_graph_class_object_created():
    return graph_class_object is not None


def is_graphviz_object_created():
    return graphviz_object is not None


def delete_graph_class_object():
    global graph_class_object
    graph_class_object = None


def delete_graphviz_object():
    global graphviz_object
    graphviz_object = None


def rebuild_graphviz_object_by_graph_class_object():
    if not is_graph_class_object_created():
        return
    create_graphviz_object(graph_class_object.is_directed)
    for node in graph_class_object.nodes:
        graphviz_object.node(node,
                             style="filled",
                             color=color_node_border,
                             fillcolor=color_node_default)
    for edge in graph_class_object.get_edges():
        graphviz_object.node(edge[0],
                             style="filled",
                             color=color_node_border,
                             fillcolor=color_node_default)
        graphviz_object.node(edge[1],
                             style="filled",
                             color=color_node_border,
                             fillcolor=color_node_default)
        graphviz_object.edge(edge[0], edge[1])


def set_non_default_colors_to_nodes(updated_nodes, colors):
    if not is_graphviz_object_created():
        return None
    if len(updated_nodes) != len(colors):
        return None

    graphviz_object_copy = graphviz.Graph(strict=True) if isinstance(graphviz_object, graphviz.Graph)\
        else graphviz.Digraph(strict=True)
    for node in graph_class_object.nodes:
        if node in updated_nodes:
            ind = updated_nodes.index(node)
            graphviz_object_copy.node(node, style="filled", color=color_node_border, fillcolor=colors[ind])
        else:
            graphviz_object_copy.node(node, style="filled", color=color_node_border, fillcolor=color_node_default)
    for edge in graph_class_object.get_edges():
        graphviz_object_copy.edge(edge[0], edge[1])
    return graphviz_object_copy
