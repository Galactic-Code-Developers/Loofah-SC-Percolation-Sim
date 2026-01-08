import argparse
from .config import SimConfig
from .geometry import generate_scaffold_graph
from .coating import apply_coating_states
from .metrics import summarize_run
from .io import write_json

def main():
    ap = argparse.ArgumentParser(description="Loofah-SC percolation simulation (reference backend).")
    ap.add_argument("--out", default="results/run.json")
    ap.add_argument("--n-nodes", type=int, default=600)
    ap.add_argument("--mean-degree", type=float, default=3.0)
    ap.add_argument("--hierarchy-levels", type=int, default=3)
    ap.add_argument("--p", type=float, default=0.65, help="coating continuity probability")
    ap.add_argument("--defect", type=float, default=0.03, help="defect probability on coated edges")
    ap.add_argument("--ts", type=float, default=1.0, help="normalized coating thickness")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    cfg = SimConfig(
        n_nodes=args.n_nodes,
        mean_degree=args.mean_degree,
        hierarchy_levels=args.hierarchy_levels,
        coating_continuity_p=args.p,
        defect_p=args.defect,
        ts=args.ts,
        seed=args.seed,
    )

    G = generate_scaffold_graph(cfg.n_nodes, cfg.mean_degree, cfg.hierarchy_levels, cfg.seed)
    H = apply_coating_states(G, cfg.coating_continuity_p, cfg.defect_p, cfg.seed)

    anchors_a = set(range(0, min(10, cfg.n_nodes)))
    anchors_b = set(range(max(0, cfg.n_nodes - 10), cfg.n_nodes))

    summary = summarize_run(H, cfg, anchors_a, anchors_b)
    write_json(args.out, summary)

if __name__ == "__main__":
    main()
