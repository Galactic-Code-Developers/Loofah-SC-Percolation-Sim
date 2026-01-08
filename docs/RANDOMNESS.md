# Randomness, seeds, and determinism

This project uses stochastic elements (graph generation, defect assignment, and coating continuity states).
To ensure reproducibility:

## RNG policy

- All stochastic draws are driven by a single integer **seed**.
- The default seed used throughout the repository is **42** unless otherwise specified.

## Deterministic behavior

Runs are deterministic given:

1. the same `SimConfig` (including `seed`),
2. the same software versions (Python + NumPy),
3. the same platform floating-point behavior (minor differences may occur across architectures).

## Recording seeds and configuration

All scripts and notebooks write summary outputs that include the full configuration (including seed) in JSON.
Example: `scripts/run_sweep.py` writes `results/sweep.json` with:

- `base_config`: the exact configuration used as the template,
- `sweep`: the per-parameter results.

## Recommended practice for paper reproduction

- Use the configs in `configs/` as canonical references.
- When producing a paper figure, record the exact config file name and seed in the figure caption or the notebook markdown cell.
