import networkx as nx
from loofah_sc_sim.transport import assign_local_ic, estimate_global_ic

def test_global_ic_zero_if_no_sc():
    G = nx.path_graph(10)
    for u, v in G.edges():
        G.edges[u, v]["sc"] = False
    assign_local_ic(G, ic_scale=1.0, ts=1.0)
    assert estimate_global_ic(G, {0}, {9}) == 0.0

def test_global_ic_positive_if_sc_path_exists():
    G = nx.path_graph(10)
    for u, v in G.edges():
        G.edges[u, v]["sc"] = True
    assign_local_ic(G, ic_scale=2.0, ts=1.0)
    assert estimate_global_ic(G, {0}, {9}) > 0.0
