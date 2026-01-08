import networkx as nx

def superconducting_subgraph(H: nx.Graph) -> nx.Graph:
    sc_edges = [(u, v) for u, v, d in H.edges(data=True) if d.get("sc", False)]
    S = nx.Graph()
    S.add_nodes_from(H.nodes())
    S.add_edges_from(sc_edges)
    return S

def largest_sc_component_size(H: nx.Graph) -> int:
    S = superconducting_subgraph(H)
    comps = list(nx.connected_components(S))
    return max((len(c) for c in comps), default=0)

def is_spanning(H: nx.Graph, anchors_a: set[int], anchors_b: set[int]) -> bool:
    """Spanning defined as any SC-connected path between anchor sets A and B."""
    S = superconducting_subgraph(H)
    for a in anchors_a:
        if a not in S:
            continue
        for b in anchors_b:
            if b not in S:
                continue
            if nx.has_path(S, a, b):
                return True
    return False
