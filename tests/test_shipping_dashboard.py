import pandas as pd

from src.analysis.analyze_data import filter_records, kpi_summary, port_performance
from src.analysis.clean_data import clean_shipping_data


def test_clean_shipping_data_removes_invalid_rows_and_fills_missing_values():
    df = pd.DataFrame(
        [
            {
                "timestamp": "2026-05-01 08:00",
                "port_name": "Singapore",
                "route": "Asia-Europe",
                "vessel_imo": "IMO1234567",
                "vessel_type": "Container",
                "turnaround_hours": "20",
                "cargo_teu": "",
                "avg_speed_knots": "18.5",
                "delay_status": "On-Time",
            },
            {
                "timestamp": "bad-date",
                "port_name": "Shanghai",
                "route": "Trans-Pacific",
                "vessel_imo": "IMO7654321",
                "vessel_type": "Container",
                "turnaround_hours": "25",
                "cargo_teu": "9000",
                "avg_speed_knots": "19.0",
                "delay_status": "Delayed",
            },
            {
                "timestamp": "2026-05-02 08:00",
                "port_name": "Tokyo",
                "route": "Intra-Asia",
                "vessel_imo": "IMO9999999",
                "vessel_type": "Tanker",
                "turnaround_hours": "-1",
                "cargo_teu": "3000",
                "avg_speed_knots": "16.0",
                "delay_status": "On-Time",
            },
        ]
    )

    result = clean_shipping_data(df, persist=False)

    assert len(result.cleaned) == 1
    assert result.cleaned["cargo_teu"].iloc[0] == 0
    assert result.cleaned["is_delayed"].iloc[0] == False


def test_analysis_filters_and_summarizes_sample_records():
    df = pd.DataFrame(
        [
            {
                "port_name": "Singapore",
                "route": "Asia-Europe",
                "vessel_type": "Container",
                "vessel_imo": "IMO1",
                "cargo_teu": 8000,
                "turnaround_hours": 18,
                "avg_speed_knots": 20,
                "is_delayed": False,
            },
            {
                "port_name": "Shanghai",
                "route": "Trans-Pacific",
                "vessel_type": "Container",
                "vessel_imo": "IMO2",
                "cargo_teu": 10000,
                "turnaround_hours": 32,
                "avg_speed_knots": 17,
                "is_delayed": True,
            },
        ]
    )

    filtered = filter_records(df, port="Shanghai", route="All", vessel_type="All", min_cargo_teu=5000)
    summary = kpi_summary(filtered)
    ports = port_performance(df)

    assert len(filtered) == 1
    assert summary["delay_rate"].iloc[0] == 100
    assert ports.iloc[0]["port_name"] == "Shanghai"
