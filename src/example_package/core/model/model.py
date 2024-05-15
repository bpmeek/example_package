import pickle
import pandas as pd

from importlib.resources import read_binary

from typing import Dict, Any

from ..data_processing.pipeline import process_data
from ...assets.conf.config import load_config


class Model:
    def __init__(self):
        self._model = pickle.loads(read_binary('example_package.assets.model', 'model.pkl'))
        self._config = load_config()

    def predict(self, data: pd.DataFrame or Dict[str, Any]):
        processed_data = process_data(data, self._config.get("CATEGORICAL_FEATURES"), self._config.get("DROP_FEATURES"))
        return self._model.predict(processed_data)
