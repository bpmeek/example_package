import pytest
import pandas as pd


@pytest.fixture()
def data_processing_input():
    return {
        "bedrooms": 4,
        "bathrooms": 2,
        "area": 7420,
        "basement": "no",
        "furnishingstatus": "furnished"
    }


@pytest.fixture()
def categorical_features_map():
    return {
        "basement": ["yes", "no"],
        "furnishingstatus": ["furnished", "semi-furnished", "unfurnished"]
    }

@pytest.fixture()
def data_processing_output():
    data = {
        "bedrooms": [4],
        "bathrooms": [2],
        "area": [7420],
        "basement_yes": [1],
        "furnishingstatus_semi-furnished": [0],
        "furnishingstatus_unfurnished": [0]
    }
    return pd.DataFrame(data=data)
