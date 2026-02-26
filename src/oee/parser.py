import pandas as pd


def load_production_data(filepath: str) -> pd.DataFrame:
    """Load production data from CSV file into a DataFrame."""
    return pd.read_csv(filepath)


def load_downtime_data(filepath: str) -> pd.DataFrame:
    """Load downtime log data from CSV file into a DataFrame."""
    return pd.read_csv(filepath)
