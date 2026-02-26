# Production OEE Analytics

Python toolkit and CLI to compute Overall Equipment Effectiveness (OEE) from production and downtime data in manufacturing lines. This project helps manufacturing engineers quantify productivity by analysing availability, performance and quality metrics.

## Features

- Calculate OEE from CSV files containing production and downtime logs.
- Break down OEE into availability, performance and quality components.
- Generate charts to visualise trends.
- Command-line interface for batch processing and integration into automation scripts.
- Modular Python API for integration into other systems.

## Installation

Clone the repository and install the package in editable mode with dependencies:

```
git clone https://github.com/Saisurya1708/production-oee-analytics.git
cd production-oee-analytics
pip install -e .
```

Alternatively, install directly from GitHub using pip:

```
pip install git+https://github.com/Saisurya1708/production-oee-analytics.git
```

## Quick start

To compute OEE for your factory dataset:

```
python -m oee.cli --production sample_data/production.csv --downtime sample_data/downtime.csv --output report.html
```

You will receive a report containing OEE metrics and charts. See the [docs](docs/index.md) for more examples.

## Repository structure

- `src/oee/` – Python package containing the OEE calculators, visualisation utilities and CLI.
- `sample_data/` – Example production and downtime CSV files.
- `tests/` – Unit tests using pytest.
- `docs/` – Project documentation generated with Sphinx.
- `oee-methodology.md` – Explanation of OEE calculation methodology and assumptions.

## Methodology

We follow the standard OEE formula where:

OEE = Availability × Performance × Quality

See [oee-methodology.md](oee-methodology.md) for details on how each component is derived from production and downtime logs.

## Contribution & support

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. For bug reports or feature requests, open an issue using the provided template.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
