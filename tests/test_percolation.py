import networkx as nx
from loofah_sc_sim.percolation import largest_sc_component_size

def test_empty_sc_component_has_size_one_due_to_nodes():
    G = nx.path_graph(10)
    for u, v in G.edges():
        G.edges[u, v]["sc"] = False
    assert largest_sc_component_size(G) == 1

def test_all_sc_component_has_full_size():
    G = nx.path_graph(10)
    for u, v in G.edges():
        G.edges[u, v]["sc"] = True
    assert largest_sc_component_size(G) == 10
