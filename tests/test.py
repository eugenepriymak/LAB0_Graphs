import unittest
from graph.graph_class import Graph


# EDG stands for 'Empty Directed Graph'
class TestEDG(unittest.TestCase):
    def test_edg_get_nodes(self):
        graph = Graph(is_directed=True)
        self.assertEqual(set(graph.get_nodes()), set())

    def test_edg_get_outgoing_nodes(self):
        graph = Graph(is_directed=True)
        self.assertEqual(graph.get_outgoing_nodes("a"), None)

    def test_edg_get_edges(self):
        graph = Graph(is_directed=True)
        self.assertEqual(set(graph.get_edges()), set())

    def test_edg_delete_node(self):
        graph = Graph(is_directed=True)
        graph.delete_node("a")
        self.assertEqual(set(graph.get_nodes()), set())

    def test_edg_delete_edge(self):
        graph = Graph(is_directed=True)
        graph.delete_edge("hello", "world")
        self.assertEqual(set(graph.get_edges()), set())


# NEDG stands for 'Non-Empty Directed Graph'
class TestNEDG(unittest.TestCase):
    def test_add_get_and_delete(self):
        graph = Graph(is_directed=True)
        nodes = {"a", "()", "hello world", "1.5"}
        edges = {("first", "second"),
                 ("a", "second"),
                 ("second", "1.5"),
                 ("second", "_third_"),
                 ("second", "a"),
                 ("()", "1.5")}

        for node in nodes:
            graph.add_node(node)
        for edge in edges:
            graph.add_edge(*edge)
        self.assertEqual(set(graph.get_nodes()), {"a", "()", "hello world", "1.5", "first", "second", "_third_"})
        self.assertEqual(set(graph.get_outgoing_nodes("second")), {"1.5", "_third_", "a"})
        self.assertEqual(set(graph.get_edges()), edges)

        graph.delete_edge("1.5", "second")
        self.assertEqual(set(graph.get_edges()), edges)
        graph.delete_edge("second", "a")
        self.assertEqual(set(graph.get_edges()), {("first", "second"),
                                                  ("a", "second"),
                                                  ("second", "1.5"),
                                                  ("second", "_third_"),
                                                  ("()", "1.5")})

        graph.delete_node("second")
        self.assertEqual(set(graph.get_edges()), {("()", "1.5")})
        self.assertEqual(set(graph.get_nodes()), {"a", "()", "hello world", "1.5", "first", "_third_"})


if __name__ == "__main__":
    unittest.main()
