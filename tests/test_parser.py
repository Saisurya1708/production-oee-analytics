"""Tests for the OEE parser utilities."""

from pathlib import Path

from oee.parser import load_production_data, load_downtime_data


def test_load_production_data(tmp_path) -> None:
    """Ensure the production CSV loader returns a DataFrame with expected columns and rows."""
    csv_path = tmp_path / "production.csv"
    csv_path.write_text("timestamp,good_count,operating_time_minutes\n2026-01-01 08:00,100,60\n")
    df = load_production_data(csv_path)
    assert list(df.columns) == ["timestamp", "good_count", "operating_time_minutes"]
    assert len(df) == 1


def test_load_downtime_data(tmp_path) -> None:
    """Ensure the downtime CSV loader returns a DataFrame with expected columns and rows."""
    csv_path = tmp_path / "downtime.csv"
    csv_path.write_text("timestamp,downtime_reason,duration_minutes\n2026-01-01 08:15,Planned Maintenance,5\n")
    df = load_downtime_data(csv_path)
    assert list(df.columns) == ["timestamp", "downtime_reason", "duration_minutes"]
    assert len(df) == 1
