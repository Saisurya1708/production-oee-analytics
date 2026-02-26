# Production OEE Analytics Documentation

Welcome to the documentation for the Production OEE analytics toolkit and CLI. This site provides guidance on installation, usage and extension of the project.

## Installation

See the project README for installation instructions. You will need Python 3.8 or later. Install dependencies with `pip install -r requirements.txt` after cloning the repository.

## Using the CLI

The toolkit includes a command‑line interface that you can invoke with:

```
python -m oee.cli --production path/to/production.csv --downtime path/to/downtime.csv
```

This command loads your production and downtime CSV files, computes Overall Equipment Effectiveness and prints the result.

## Library Modules

- **`oee.parser`** – Functions for loading production and downtime data from CSV files into pandas DataFrames.
- **`oee.analysis`** – Functions for calculating Overall Equipment Effectiveness and its components.
- **`oee.charts`** – Visualization utilities for plotting OEE metrics over time.

## Extending the Package

We welcome contributions! You can extend this package by adding new analysis functions, additional CLI commands or improved visualizations. Please include unit tests for new features and follow the contribution guidelines in `CONTRIBUTING.md`.
