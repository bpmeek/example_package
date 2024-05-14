from ...core.data_processing.pipeline import process_data
import numpy as np


def test_process_data(data_processing_input, categorical_features_map, data_processing_output):
    actual = process_data(data_processing_input, categorical_features_map)
    assert np.all(actual.eq(data_processing_output)), f"Expected{data_processing_output}\nReceived\n{actual}"
