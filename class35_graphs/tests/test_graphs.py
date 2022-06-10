import pytest
from class35_graphs.class35_graphs.graphs import Graph, Vertex

def test_add_node():
    graph = Graph()
    graph.add_node('A')
    assert graph.adjacency_list['A'] is not None

def test_add_node_2(graph):
    graph.add_node(1)
    assert graph.adjacency_list[1] is not None

def test_add_edge(graph):
    graph.add_edge('E', 'F')
    assert graph.adjacency_list['E'].edges == ['F']

def test_get_nodes(graph):
    assert graph.get_nodes() == {'A', 'B', 'C', 'D', 'E', 'F'}

def test_get_nodes_empty():
    graph = Graph()
    assert graph.get_nodes() == {}

def test_get_neighbors(graph):
    assert graph.get_neighbors('A') == ['B', 'C']

def test_get_neighbors_empty(graph):
    assert graph.get_neighbors('F') == []

def test_size(graph):
    assert graph.size() == 6

def test_size_empty():
    graph = Graph()
    assert graph.size() == 0

def test_breadth_first(graph):
    assert graph.breadth_first('A') == ['A', 'B', 'C', 'D', 'E', 'F']

def test_print_empty_graph(graph2):
    assert graph2.__str__() == 'Null'

def test_print_graph(graph):
    assert graph.__str__() == 'vertex :  edges \nA      :  [B, C]  \nB      :  [A]  \nC      :  [A]  \nD      :  [A]  \nE      :  [F]  \nF      :  [E]  \n'

def test_print_graph_one_node(graph3):
    assert graph3.__str__() == 'vertex :  edges \nA      :  []  \n'

def test_edge_with_weight(graph4):
    assert graph4.__str__() == 'vertex :  edges \n1      :  [(2,5)]  \n2      :  [(1, 5)]  \n'


@pytest.fixture
def graph():
    g = Graph()
    g.add_node('A')
    g.add_node('B')
    g.add_node('C')
    g.add_node('D')
    g.add_node('E')
    g.add_node('F')
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'D')
    return g


@pytest.fixture
def graph2():
    g = Graph()
    return g


@pytest.fixture
def graph3():
    g = Graph()
    g.add_node(1)
    return g


@pytest.fixture
def graph4():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_edge(1, 2, 5)
    return g