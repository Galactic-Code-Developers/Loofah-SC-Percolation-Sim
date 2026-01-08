import random
import networkx as nx

def apply_coating_states(G: nx.Graph, continuity_p: float, defect_p: float, seed: int) -> nx.Graph:
    """Mark edges as superconducting-coated (SC) or not.

    SC edge occurs with probability continuity_p, then may fail due to defect_p.
    """
    rng = random.Random(seed)
    H = G.copy()
    for u, v in H.edges():
        sc = (rng.random() < continuity_p)
        if sc and (rng.random() < defect_p):
            sc = False
        H.edges[u, v]["sc"] = sc
    return H
