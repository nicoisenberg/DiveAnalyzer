import pandas as pd

from src.validation import validate_not_empty

def test_validate_not_empty_with_data():

    data = pd.DataFrame({
        "Depth": [20]
    })

    result = validate_not_empty(data)

    assert result is True


def test_validate_not_empty_with_empty_dataframe():

    data = pd.DataFrame()

    result = validate_not_empty(data)

    assert result is False