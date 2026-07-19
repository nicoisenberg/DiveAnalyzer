import pandas as pd

from src.plotting import save_plot


def test_save_plot(tmp_path):

    data = pd.DataFrame({
        "Date": ["2026-01-01", "2026-01-02"],
        "Depth": [20 , 30],
        "Temperature": [24, 20]
    })

    output_path = tmp_path / "test_plot.png"

    save_plot(
        data=data,
        x_column="Date",
        y_columns=["Depth", "Temperature"],
        output_path=output_path,
        title="Test Plot",
        y_label="Value"
    )

    assert output_path.exists()
    assert output_path.stat().st_size > 0