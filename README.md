# Loofah-SC-Percolation-Sim

Simulation-first reference implementation for **percolation-controlled superconducting transport**
on **loofah-templated biomorphic carbon architectures** with conformal superconducting coatings.

This repository supports the 2026 simulation-first manuscript:

**Antonios Valamontes (2026)**  
*Loofah-Templated Biomorphic Carbon Superconducting Composites: A Simulation-Driven Platform for Percolation-Controlled Transport Predictions*.

## What this repo contains

- **Geometry**: stochastic, loofah-like hierarchical network generator (`src/loofah_sc_sim/geometry.py`)
- **Coating continuity & defects**: binary superconducting state model (`src/loofah_sc_sim/coating.py`)
- **Percolation**: spanning-cluster detection (`src/loofah_sc_sim/percolation.py`)
- **Transport proxy**: bottleneck-constrained critical current estimator (`src/loofah_sc_sim/transport.py`)
- **Reproducible outputs**: JSON summaries embedding full configuration (`src/loofah_sc_sim/io.py`)
- **Notebooks**: Colab-ready notebooks reproducing the numerical workflow (`notebooks/`)
- **Tests**: lightweight unit tests for percolation and transport logic (`tests/`)

The workflow schematic in the manuscript is produced in LaTeX (TikZ); numerical sweeps and summaries are produced here.

## Quick start (Google Colab)

1. Open `notebooks/00_Colab_Setup.ipynb`
2. Run notebooks in order:

- `00_Colab_Setup.ipynb`
- `01_Scaffold_Generation.ipynb`
- `02_Coating_and_Percolation.ipynb`
- `03_Transport_and_Ic.ipynb`
- `04_Parameter_Sweep.ipynb`

This reproduces the main numerical outputs and generates JSON summaries under `results/`.

## Local install (recommended)

### Option A: conda (environment.yml)

```bash
conda env create -f environment.yml
conda activate loofah-sc-sim
python -m pip install -e .
```

### Option B: pip

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -e .
```

## Reproducing the paper outputs

### Canonical configurations

Reference configurations are provided under `configs/`:

- `configs/paper_small_fast.json` (fast smoke test)
- `configs/paper_nominal.json` (nominal)
- `configs/sweep_recipe.json` (parameter sweep recipe)

### Command-line sweep (produces sweep.json)

```bash
python scripts/run_sweep.py --out results/sweep.json --n-realizations 100 --seed 42
```

### Single case (sanity check)

```bash
python scripts/make_one_case.py --out results/one_case.json --seed 42
```

## Determinism and randomness

All runs are deterministic under fixed random seeds.
See `docs/RANDOMNESS.md` for the seed policy and reproducibility expectations.

## Figure ↔ code mapping

See `docs/FIGURE_MAP.md` for a direct mapping between paper artifacts and the repository.

## Repository layout

- `src/loofah_sc_sim/` – core library
- `scripts/` – CLI helpers (single case, sweep)
- `notebooks/` – Colab-ready reproduction notebooks
- `configs/` – canonical configurations used for reproduction
- `results/` – generated outputs (JSON summaries)
- `docs/` – reproducibility notes

## License

MIT (see `LICENSE`).

## Citation

If you use this repository, please cite the associated manuscript and/or the repository archive.
A `CITATION.cff` file is included for GitHub citation support.
