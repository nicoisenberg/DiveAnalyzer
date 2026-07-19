from src.loader import load_csv


def test_load_csv_with_existing_file(tmp_path):

    csv_path = tmp_path / "test_data.csv"

    csv_path.write_text(
        "Date,Depth,Temperature\n"
        "2026-01-01,20,24\n",
        encoding="utf-8"
    )

    result = load_csv(csv_path)

    assert result is not None
    assert len(result) == 1
    assert list(result.columns) == ["Date", "Depth", "Temperature"]

    