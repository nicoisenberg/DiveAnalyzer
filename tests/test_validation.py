import pandas as pd

from src.validation import validate_not_empty, validate_required_columns

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


def test_validate_required_columns_with_existing_columns():
    
    data = pd.DataFrame({
        "Depth": [20]
    })

    result = validate_required_columns(data, ["Depth"])

    assert result is True


def test_validate_required_columns_with_missing_columns():

    data = pd.DataFrame({
        "Temperature": [20]
    })

    result = validate_required_columns(data, ["Depth"])

    assert result is False