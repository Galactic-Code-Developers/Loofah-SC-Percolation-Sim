import argparse
from loofah_sc_sim.config import SimConfig
from loofah_sc_sim.geometry import generate_scaffold_graph
from loofah_sc_sim.coating import apply_coating_states
from loofah_sc_sim.metrics import summarize_run
from loofah_sc_sim.io import write_json

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="results/sweep.json")
    ap.add_argument("--n-realizations", type=int, default=100)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    cfg0 = SimConfig(seed=args.seed)
    anchors_a = set(range(0, 10))
    anchors_b = set(range(cfg0.n_nodes - 10, cfg0.n_nodes))

    ps = [i / 20.0 for i in range(0, 21)]
    runs = []

    for p in ps:
        spanning = 0
        ic_sum = 0.0
        for k in range(args.n_realizations):
            cfg = SimConfig(
                n_nodes=cfg0.n_nodes,
                mean_degree=cfg0.mean_degree,
                hierarchy_levels=cfg0.hierarchy_levels,
                coating_continuity_p=p,
                defect_p=cfg0.defect_p,
                ts=cfg0.ts,
                ic_scale=cfg0.ic_scale,
                seed=cfg0.seed + k,
            )
            G = generate_scaffold_graph(cfg.n_nodes, cfg.mean_degree, cfg.hierarchy_levels, cfg.seed)
            H = apply_coating_states(G, cfg.coating_continuity_p, cfg.defect_p, cfg.seed)
            s = summarize_run(H, cfg, anchors_a, anchors_b)
            spanning += int(s["is_spanning"])
            ic_sum += s["estimated_global_ic"]

        runs.append({
            "p": p,
            "spanning_fraction": spanning / args.n_realizations,
            "mean_estimated_global_ic": ic_sum / args.n_realizations,
        })

    write_json(args.out, {"base_config": cfg0.__dict__, "sweep": runs})

if __name__ == "__main__":
    main()
