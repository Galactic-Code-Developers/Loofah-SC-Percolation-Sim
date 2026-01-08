import random
import networkx as nx

def generate_scaffold_graph(n_nodes: int, mean_degree: float, hierarchy_levels: int, seed: int) -> nx.Graph:
    """Generate a loofah-like hierarchical open-cell scaffold as a graph.

    This is a reference backend: it enforces hierarchical connectivity by mixing
    a sparse base graph with higher-density local clusters. It is intended as a
    method-neutral proxy compatible with later FEM or lattice backends.
    """
    rng = random.Random(seed)

    # Base sparse random graph
    p = min(1.0, max(0.0, mean_degree / max(1, n_nodes - 1)))
    G = nx.fast_gnp_random_graph(n_nodes, p, seed=seed, directed=False)

    # Add hierarchical clustering
    for level in range(max(1, hierarchy_levels)):
        n_centers = max(2, n_nodes // (50 * (level + 1)))
        centers = rng.sample(range(n_nodes), n_centers)
        radius = max(10, n_nodes // (20 * (level + 1)))

        for c in centers:
            nbrs = {c}
            while len(nbrs) < min(radius, n_nodes):
                nbrs.add(rng.randrange(n_nodes))
            nbrs = list(nbrs)

            # connect within neighborhood to increase clustering
            prob = 0.02 * (level + 1)
            for i in range(len(nbrs)):
                for j in range(i + 1, len(nbrs)):
                    if rng.random() < prob:
                        G.add_edge(nbrs[i], nbrs[j])

    # Ensure connectivity by linking components minimally
    comps = list(nx.connected_components(G))
    if len(comps) > 1:
        comps = [list(c) for c in comps]
        for i in range(len(comps) - 1):
            G.add_edge(rng.choice(comps[i]), rng.choice(comps[i + 1]))

    return G
