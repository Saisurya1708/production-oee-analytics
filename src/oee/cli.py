"""Command-line interface for the OEE analytics package.

This module provides a CLI for computing Overall Equipment Effectiveness (OEE)
from production and downtime CSV files. It loads the CSVs using the parser
utilities, computes OEE via the analysis module, and prints the result.

Usage example:

    python -m oee.cli --production path/to/production.csv --downtime path/to/downtime.csv

"""

import argparse

from .parser import load_production_data, load_downtime_data
from .analysis import calculate_oee


def main() -> None:
    """Parse command-line arguments and compute OEE."""
    parser = argparse.ArgumentParser(
        description="Compute Overall Equipment Effectiveness (OEE) from production and downtime data."
    )
    parser.add_argument(
        "--production",
        required=True,
        help="Path to the CSV file containing production counts and operating time.",
    )
    parser.add_argument(
        "--downtime",
        required=True,
        help="Path to the CSV file containing unplanned downtime information.",
    )

    args = parser.parse_args()

    # Load the input data
    production_df = load_production_data(args.production)
    downtime_df = load_downtime_data(args.downtime)

    # Compute OEE using the analysis module
    oee_score = calculate_oee(production_df, downtime_df)

    # Print the result as a percentage with two decimal places
    print(f"Overall Equipment Effectiveness (OEE): {oee_score:.2%}")


if __name__ == "__main__":
    main()
