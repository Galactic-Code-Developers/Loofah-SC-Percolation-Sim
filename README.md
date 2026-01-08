# Loofah-SC-Percolation-Sim

Reference, simulation-first repository supporting the manuscript:

**Loofah-Templated Biomorphic Carbon Superconducting Composites: A Simulation-Driven Platform for Percolation-Controlled Transport Predictions**

This repository provides a **graph-theoretic reference backend** (method-neutral by design) to:
1) generate a hierarchical scaffold graph (loofah-like connectivity proxy),
2) apply a superconducting coating continuity model,
3) compute percolation/spanning behavior,
4) estimate transport bottlenecks and effective critical current scaling.

## Quickstart (local)

### Conda (recommended)
```bash
conda env create -f environment.yml
conda activate loofah-sc-sim
python -m loofah_sc_sim.cli --help
```

### pip
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m loofah_sc_sim.cli --help
```

## Example: run a small sweep
```bash
python scripts/run_sweep.py --out results/demo_sweep.json --n-realizations 50
```

## Colab
See `notebooks/00_Colab_Setup.ipynb` and the subsequent notebooks. They are designed to run with `pip install` in Colab.

## Reproducibility
All runs are seeded. Outputs embed configuration in JSON.

## License
MIT (see `LICENSE`).
