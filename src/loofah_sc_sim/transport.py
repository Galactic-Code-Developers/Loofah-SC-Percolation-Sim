import networkx as nx

def assign_local_ic(H: nx.Graph, ic_scale: float, ts: float) -> None:
    """Assign normalized local critical current to SC edges.

    Reference model: Ic ~ ic_scale * ts (normalized). Extend later with geometry weights.
    """
    for u, v, d in H.edges(data=True):
        if d.get("sc", False):
            d["ic"] = float(ic_scale) * max(0.0, float(ts))
        else:
            d["ic"] = 0.0

def bottleneck_ic_on_path(H: nx.Graph, path: list[int]) -> float:
    ics = []
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        ics.append(H.edges[u, v].get("ic", 0.0))
    return min(ics) if ics else 0.0

def estimate_global_ic(H: nx.Graph, anchors_a: set[int], anchors_b: set[int]) -> float:
    """Estimate global Ic as maximum bottleneck Ic over candidate SC paths.

    Candidate paths are approximated via shortest-path search on the SC subgraph.
    """
    S = nx.Graph()
    S.add_nodes_from(H.nodes())
    S.add_edges_from([(u, v) for u, v, d in H.edges(data=True) if d.get("sc", False)])

    best = 0.0
    for a in anchors_a:
        for b in anchors_b:
            if a in S and b in S:
                try:
                    path = nx.shortest_path(S, a, b)
                except nx.NetworkXNoPath:
                    continue
                best = max(best, bottleneck_ic_on_path(H, path))
    return float(best)
