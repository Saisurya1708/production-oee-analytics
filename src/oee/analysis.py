import pandas as pd


def calculate_oee(production: pd.DataFrame, downtime: pd.DataFrame) -> float:
    """
    Compute Overall Equipment Effectiveness (OEE) from production and downtime data.

    Availability is calculated as (Total operating time - Unplanned downtime) / Total operating time.
    Performance and quality metrics are placeholders (1.0) and can be extended based on actual data.

    Args:
        production: DataFrame with a column named "operating_time_minutes" and optionally "good_count".
        downtime: DataFrame with a column named "duration" representing unplanned downtime.

    Returns:
        float: OEE ratio between 0 and 1.
    """
    # Sum the operating time in minutes
    total_time = production["operating_time_minutes"].sum()
    # Sum the unplanned downtime durations
    unplanned_downtime = downtime["duration"].sum()

    # Compute availability, avoiding division by zero
    if total_time == 0:
        availability = 0.0
    else:
        availability = (total_time - unplanned_downtime) / total_time

    # TODO: Compute performance and quality based on production data (e.g., good_count and ideal_cycle_time)
    performance = 1.0
    quality = 1.0

    return availability * performance * quality
