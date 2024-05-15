from ...core.data_processing.functions import check_dataframe, encode, drop_first

import numpy as np


def test_check_dataframe(data_processing_input, check_dataframe_output):
    actual = check_dataframe(data_processing_input)
    assert np.all(actual.eq(check_dataframe_output)), f"Expected\n{check_dataframe_output}\nbut got\n{actual}"


def test_encode(encode_df, encode_categorical_features, encode_output):
    actual = encode(encode_df, encode_categorical_features)
    assert np.all(actual.eq(encode_output)), f"Expected\n{encode_output}\nbut got\n{actual}"


def test_drop_first(drop_first_input, drop_features, drop_first_output):
    actual = drop_first(drop_first_input, drop_features)
    assert np.all(actual.eq(drop_first_output)), f"Expcted\n{drop_first_output}\nbut got\n{actual}"
