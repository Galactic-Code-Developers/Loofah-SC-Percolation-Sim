from dataclasses import asdict
from .percolation import largest_sc_component_size, is_spanning
from .transport import assign_local_ic, estimate_global_ic

def summarize_run(H, cfg, anchors_a, anchors_b):
    assign_local_ic(H, ic_scale=cfg.ic_scale, ts=cfg.ts)
    return {
        "config": asdict(cfg),
        "largest_sc_component": int(largest_sc_component_size(H)),
        "is_spanning": bool(is_spanning(H, anchors_a, anchors_b)),
        "estimated_global_ic": float(estimate_global_ic(H, anchors_a, anchors_b)),
    }
