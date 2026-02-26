import pandas as pd
import matplotlib.pyplot as plt


def plot_oee_over_time(oee_values: pd.Series, timestamps: pd.Series) -> None:
    """Plot OEE over time.

    Args:
        oee_values (pd.Series): Series of OEE values.
        timestamps (pd.Series): Corresponding timestamps.
    """
    plt.figure()
    plt.plot(timestamps, oee_values)
    plt.title("OEE Over Time")
    plt.xlabel("Time")
    plt.ylabel("OEE")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
