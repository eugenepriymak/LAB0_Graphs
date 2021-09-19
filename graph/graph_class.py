class Graph:
    EDGE_IS_NOT_PRESENT = 0
    EDGE_IS_PRESENT = 1

    def __init__(self, is_directed):
        self.is_directed = is_directed
        self.nodes = []
        self.adj_matr = []

    def add_node(self, node):
        def create_matr_line():
            if self.adj_matr == []:
                self.adj_matr.append([Graph.EDGE_IS_NOT_PRESENT])
            else:
                columns_number = len(self.adj_matr[0])
                self.adj_matr.append([Graph.EDGE_IS_NOT_PRESENT] * columns_number)

        def create_matr_column():
            if self.adj_matr == []:
                self.adj_matr.append([Graph.EDGE_IS_NOT_PRESENT])
            else:
                for matr_line in self.adj_matr:
                    matr_line.append(Graph.EDGE_IS_NOT_PRESENT)
        if node in self.nodes:
            return
        self.nodes.append(node)
        if self.adj_matr == []:
            create_matr_line()
        else:
            create_matr_line()
            create_matr_column()

    def delete_node(self, node):
        def delete_matr_string(ind):
            self.adj_matr.pop(ind)

        def delete_matr_column(ind):
            for matr_string in self.adj_matr:
                matr_string.pop(ind)

        if node not in self.nodes:
            return
        ind = self.nodes.index(node)
        delete_matr_string(ind)
        delete_matr_column(ind)
        self.nodes.remove(node)

    def add_edge(self, node_from, node_to):
        self.add_node(node_from)
        self.add_node(node_to)
        ind_from = self.nodes.index(node_from)
        ind_to = self.nodes.index(node_to)
        self.adj_matr[ind_from][ind_to] = Graph.EDGE_IS_PRESENT
        if not self.is_directed:
            self.adj_matr[ind_to][ind_from] = Graph.EDGE_IS_PRESENT

    def delete_edge(self, node_from, node_to):
        if node_from not in self.nodes or node_to not in self.nodes:
            return
        ind_from = self.nodes.index(node_from)
        ind_to = self.nodes.index(node_to)
        self.adj_matr[ind_from][ind_to] = Graph.EDGE_IS_NOT_PRESENT
        if not self.is_directed:
            self.adj_matr[ind_to][ind_from] = Graph.EDGE_IS_NOT_PRESENT

    def get_outgoing_nodes(self, node_from):
        if node_from not in self.nodes:
            return None
        outgoing_nodes = []
        node_from_ind = self.nodes.index(node_from)
        for ind in range(len(self.nodes)):
            if self.adj_matr[node_from_ind][ind] == Graph.EDGE_IS_PRESENT:
                outgoing_nodes.append(self.nodes[ind])
        return outgoing_nodes

    def get_nodes(self):
        return self.nodes

    def is_edge_there(self, node_from, node_to):
        if node_from not in self.nodes or node_to not in self.nodes:
            return False
        ind_from = self.nodes.index(node_from)
        ind_to = self.nodes.index(node_to)
        return True if self.adj_matr[ind_from][ind_to] == Graph.EDGE_IS_PRESENT else False

    def get_edges(self):
        def get_edges_in_directed():
            edges = []
            n_nodes = len(self.nodes)
            for line_ind in range(n_nodes):
                for column_ind in range(n_nodes):
                    if self.adj_matr[line_ind][column_ind] == Graph.EDGE_IS_PRESENT:
                        edge = (self.nodes[line_ind], self.nodes[column_ind])
                        edges.append(edge)
            return edges

        def get_edges_in_non_directed():
            edges = []
            n_nodes = len(self.nodes)
            for line_ind in range(n_nodes):
                for column_ind in range(line_ind + 1):
                    if self.adj_matr[line_ind][column_ind] == Graph.EDGE_IS_PRESENT:
                        edge = (self.nodes[line_ind], self.nodes[column_ind])
                        edges.append(edge)
            return edges

        return get_edges_in_directed() if self.is_directed else get_edges_in_non_directed()
