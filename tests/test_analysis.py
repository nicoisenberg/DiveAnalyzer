import pandas as pd

from src.analysis import generate_dive_report


def test_generate_dive_report():

    data = pd.DataFrame({
        "Date": ["2026-01-01", "2026-01-02"],
        "Depth": [20, 30],
        "Temperature": [24, 20]
    })

    result = generate_dive_report(data)

    expected_report = (
        "-----Dive Report -----\n\n"
        "Number of dives: 2\n"
        "Average depth: 25.0 m\n"
        "Maximum depth: 30.0 m\n"
        "Minimum depth: 20.0 m\n"
        "Average temperature: 22.0 °C"
    )

    assert result == expected_report
