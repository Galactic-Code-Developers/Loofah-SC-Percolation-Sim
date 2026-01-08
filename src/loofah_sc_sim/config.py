from dataclasses import dataclass

@dataclass(frozen=True)
class SimConfig:
    n_nodes: int = 600
    mean_degree: float = 3.0
    hierarchy_levels: int = 3
    coating_continuity_p: float = 0.65
    defect_p: float = 0.03
    ts: float = 1.0              # normalized coating thickness
    ic_scale: float = 1.0        # normalized Ic proportionality constant
    seed: int = 42
