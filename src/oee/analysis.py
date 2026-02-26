import pandas as pd


def calculate_oee(production: pd.DataFrame, downtime: pd.DataFrame) -> float:
    """Compute Overall Equipment Effectiveness (OEE) from production and downtime data.

    Availability = (Total time - Unplanned downtime) / Total time
    Performance = 1 (placeholder)
    Quality = 1 (placeholder)

    Returns:
        float: OEE ratio between 0 and 1.
    """
    total_time = production["elapsed_time"].sum()
    total_units = production["units_produced"].sum()
    unplanned_downtime = downtime["duration"].sum()

    availability = (total_time - unplanned_downtime) / total_time if total_time else 0.0
    # TODO: compute performance and quality metrics based on production data
    performance = 1.0
    quality = 1.0

    return availability * performance * quality
