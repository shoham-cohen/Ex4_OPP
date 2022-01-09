from unittest import TestCase
from src.DiGraph import DiGraph
from src.EdgeData import EdgeData
from src.NodeData import NodeData
from src.position import position



class TestDiGraph(TestCase):

    def test_v_size(self):
        edge1 = EdgeData(1, 0, 2)
        edge2 = EdgeData(2, 0, 1)
        edge3 = EdgeData(1, 0, 3)
        d1 = {"1,2": edge1, "2,1": edge2}
        d2 = {"2,1": edge2, "1,2": edge1}
        d3 = {"1,3": edge3}
        d4 = dict()
        node1 = NodeData(position("1.3,1.3,0"), 1, d1)
        node2 = NodeData(position("1.3,1.3,0"), 2, d2)
        node3 = NodeData(position("1.3,1.3,0"), 3, d3)
        node4 = NodeData(position("1.3,1.3,0"), 4, d4)
        dict_of_nodes = {1: node1, 2: node2, 3: node3, 4: node4}
        graph: DiGraph = DiGraph()
        graph.setVal(dict_of_nodes, 3, 0)
        self.assertEqual(graph.v_size(), 4)

    def test_e_size(self):
        edge1 = EdgeData(1, 0, 2)
        edge2 = EdgeData(2, 0, 1)
        edge3 = EdgeData(1, 0, 3)
        d1 = {"1,2": edge1, "2,1": edge2}
        d2 = {"2,1": edge2, "1,2": edge1}
        d3 = {"1,3": edge3}
        d4 = dict()
        node1 = NodeData(position("1.3,1.3,0"), 1, d1)
        node2 = NodeData(position("1.3,1.3,0"), 2, d2)
        node3 = NodeData(position("1.3,1.3,0"), 3, d3)
        node4 = NodeData(position("1.3,1.3,0"), 4, d4)
        dict_of_nodes = {1: node1, 2: node2, 3: node3, 4: node4}
        graph: DiGraph = DiGraph()
        graph.setVal(dict_of_nodes, 3, 0)
        self.assertEqual(graph.e_size(), 3)
        graph.add_edge(3, 1, 1.3)
        self.assertEqual(graph.e_size(), 4)

    def test_get_all_v(self):
        edge1 = EdgeData(1, 0, 2)
        edge2 = EdgeData(2, 0, 1)
        edge3 = EdgeData(1, 0, 3)
        d1 = {"1,2": edge1, "2,1": edge2}
        d2 = {"2,1": edge2, "1,2": edge1}
        d3 = {"1,3": edge3}
        d4 = dict()
        node1 = NodeData(position("1.3,1.3,0"), 1, d1)
        node2 = NodeData(position("1.3,1.3,0"), 2, d2)
        node3 = NodeData(position("1.3,1.3,0"), 3, d3)
        node4 = NodeData(position("1.3,1.3,0"), 4, d4)
        dict_of_nodes = {1: node1, 2: node2, 3: node3, 4: node4}
        graph: DiGraph = DiGraph()
        graph.setVal(dict_of_nodes, 3, 0)
        self.assertEqual(graph.get_all_v().get(1), node1)
        self.assertEqual(graph.get_all_v().get(2), node2)
        self.assertEqual(graph.get_all_v().get(3), node3)
        self.assertEqual(len(graph.get_all_v()), 4)

    def test_all_in_edges_of_node(self):
        edge1 = EdgeData(1, 0, 2)
        edge2 = EdgeData(2, 0, 1)
        edge3 = EdgeData(1, 0, 3)
        d1 = {"1,2": edge1, "2,1": edge2}
        d2 = {"2,1": edge2, "1,2": edge1}
        d3 = {"1,3": edge3}
        d4 = dict()
        node1 = NodeData(position("1.3,1.3,0"), 1, d1)
        node2 = NodeData(position("1.3,1.3,0"), 2, d2)
        node3 = NodeData(position("1.3,1.3,0"), 3, d3)
        node4 = NodeData(position("1.3,1.3,0"), 4, d4)
        dict_of_nodes = {1: node1, 2: node2, 3: node3, 4: node4}
        graph: DiGraph = DiGraph()
        graph.setVal(dict_of_nodes, 3, 0)
        self.assertEqual(graph.all_in_edges_of_node(1).get(2), edge2.w)

    def test_all_out_edges_of_node(self):
        edge1 = EdgeData(1, 0, 2)
        edge2 = EdgeData(2, 0, 1)
        edge3 = EdgeData(1, 0, 3)
        d1 = {"1,2": edge1, "2,1": edge2}
        d2 = {"2,1": edge2, "1,2": edge1}
        d3 = {"1,3": edge3}
        d4 = dict()
        node1 = NodeData(position("1.3,1.3,0"), 1, d1)
        node2 = NodeData(position("1.3,1.3,0"), 2, d2)
        node3 = NodeData(position("1.3,1.3,0"), 3, d3)
        node4 = NodeData(position("1.3,1.3,0"), 4, d4)
        dict_of_nodes = {1: node1, 2: node2, 3: node3, 4: node4}
        graph: DiGraph = DiGraph()
        graph.setVal(dict_of_nodes, 3, 0)
        self.assertEqual(len(graph.all_out_edges_of_node(1)), 1)

    def test_get_mc(self):
        edge1 = EdgeData(1, 0, 2)
        edge2 = EdgeData(2, 0, 1)
        edge3 = EdgeData(1, 0, 3)
        d1 = {"1,2": edge1, "2,1": edge2}
        d2 = {"2,1": edge2, "1,2": edge1}
        d3 = {"1,3": edge3}
        d4 = dict()
        node1 = NodeData(position("1.3,1.3,0"), 1, d1)
        node2 = NodeData(position("1.3,1.3,0"), 2, d2)
        node3 = NodeData(position("1.3,1.3,0"), 3, d3)
        node4 = NodeData(position("1.3,1.3,0"), 4, d4)
        dict_of_nodes = {1: node1, 2: node2, 3: node3, 4: node4}
        graph: DiGraph = DiGraph()
        graph.setVal(dict_of_nodes, 3, 0)
        self.assertEqual(graph.get_mc(), 0)

    def test_add_edge(self):
        edge1 = EdgeData(1, 0, 2)
        edge2 = EdgeData(2, 0, 1)
        edge3 = EdgeData(1, 0, 3)
        d1 = {"1,2": edge1, "2,1": edge2}
        d2 = {"2,1": edge2, "1,2": edge1}
        d3 = {"1,3": edge3}
        d4 = dict()
        node1 = NodeData(position("1.3,1.3,0"), 1, d1)
        node2 = NodeData(position("1.3,1.3,0"), 2, d2)
        node3 = NodeData(position("1.3,1.3,0"), 3, d3)
        node4 = NodeData(position("1.3,1.3,0"), 4, d4)
        dict_of_nodes = {1: node1, 2: node2, 3: node3, 4: node4}
        graph: DiGraph = DiGraph()
        graph.setVal(dict_of_nodes, 3, 0)
        self.assertTrue(graph.add_edge(3, 1, 1.3))
        self.assertFalse(graph.add_edge(5, 1, 1.3))

    def test_add_node(self):
        edge1 = EdgeData(1, 0, 2)
        edge2 = EdgeData(2, 0, 1)
        edge3 = EdgeData(1, 0, 3)
        d1 = {"1,2": edge1, "2,1": edge2}
        d2 = {"2,1": edge2, "1,2": edge1}
        d3 = {"1,3": edge3}
        d4 = dict()
        node1 = NodeData(position("1.3,1.3,0"), 1, d1)
        node2 = NodeData(position("1.3,1.3,0"), 2, d2)
        node3 = NodeData(position("1.3,1.3,0"), 3, d3)
        node4 = NodeData(position("1.3,1.3,0"), 4, d4)
        dict_of_nodes = {1: node1, 2: node2, 3: node3, 4: node4}
        graph: DiGraph = DiGraph()
        graph.setVal(dict_of_nodes, 3, 0)
        self.assertFalse(graph.add_node(4, (1.5, 1.4, 0)))

    def test_remove_node(self):
        edge1 = EdgeData(1, 0, 2)
        edge2 = EdgeData(2, 0, 1)
        edge3 = EdgeData(1, 0, 3)
        d1 = {"1,2": edge1, "2,1": edge2}
        d2 = {"2,1": edge2, "1,2": edge1}
        d3 = {"1,3": edge3}
        d4 = dict()
        node1 = NodeData(position("1.3,1.3,0"), 1, d1)
        node2 = NodeData(position("1.3,1.3,0"), 2, d2)
        node3 = NodeData(position("1.3,1.3,0"), 3, d3)
        node4 = NodeData(position("1.3,1.3,0"), 4, d4)
        dict_of_nodes = {1: node1, 2: node2, 3: node3, 4: node4}
        graph: DiGraph = DiGraph()
        graph.setVal(dict_of_nodes, 3, 0)
        self.assertTrue(graph.remove_node(5))

    def test_remove_edge(self):
        edge1 = EdgeData(1, 0, 2)
        edge2 = EdgeData(2, 0, 1)
        edge3 = EdgeData(1, 0, 3)
        d1 = {"1,2": edge1, "2,1": edge2}
        d2 = {"2,1": edge2, "1,2": edge1}
        d3 = {"1,3": edge3}
        d4 = dict()
        node1 = NodeData(position("1.3,1.3,0"), 1, d1)
        node2 = NodeData(position("1.3,1.3,0"), 2, d2)
        node3 = NodeData(position("1.3,1.3,0"), 3, d3)
        node4 = NodeData(position("1.3,1.3,0"), 4, d4)
        dict_of_nodes = {1: node1, 2: node2, 3: node3, 4: node4}
        graph: DiGraph = DiGraph()
        graph.setVal(dict_of_nodes, 3, 0)
        self.assertTrue(graph.remove_edge(1, 2))
        self.assertFalse(graph.remove_edge(8, 2))