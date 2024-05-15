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
def check_dataframe_output(data_processing_input):
    new_dict = {k: [v] for k, v in data_processing_input.items()}
    return pd.DataFrame.from_dict(new_dict)


@pytest.fixture()
def encode_df():
    df = pd.DataFrame({
        "index": [1, 2, 3],
        "categorical": ["a", "a", "a"]
    })
    return df


@pytest.fixture()
def encode_categorical_features():
    return ["categorical_b"]


@pytest.fixture()
def encode_output():
    df = pd.DataFrame({
        "index": [1, 2, 3],
        "categorical_a": [1, 1, 1],
        "categorical_b": [0, 0, 0]
    })
    return df


@pytest.fixture()
def drop_first_input():
    df = pd.DataFrame({
        "index": [1, 2, 3],
    })
    df["keep"] = "keep"
    df["drop"] = "drop"
    return df


@pytest.fixture()
def drop_features():
    return ["drop"]


@pytest.fixture()
def drop_first_output():
    df = pd.DataFrame({
        "index": [1, 2, 3],
    })
    df["keep"] = "keep"
    return df


@pytest.fixture()
def continuous_features():
    return [""]


@pytest.fixture()
def categorical_features():
    return ["basement_no", "furnishingstatus_semi-furnished", "furnishingstatus_unfurnished"]


@pytest.fixture()
def categorical_drop_features():
    return ["basement_yes", "furnishingstatus_furnished"]


@pytest.fixture()
def data_processing_output():
    data = {
        "bedrooms": [4],
        "bathrooms": [2],
        "area": [7420],
        "basement_no": [1],
        "furnishingstatus_semi-furnished": [0],
        "furnishingstatus_unfurnished": [0]
    }
    return pd.DataFrame(data=data)
