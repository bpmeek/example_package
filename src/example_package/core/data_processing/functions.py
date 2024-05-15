import pandas as pd

from typing import Dict, Any, List

from collections.abc import Mapping


def check_dataframe(data: pd.DataFrame or Dict[str, Any]) -> pd.DataFrame:
    if isinstance(data, Mapping):
        return pd.DataFrame(index=[0], data=data)
    return data


def encode(df: pd.DataFrame, categorical_features: List[str]) -> pd.DataFrame:
    encoded = pd.get_dummies(df, dtype=int)
    for col in categorical_features:
        if col not in encoded:
            encoded[col] = 0
    return encoded


def drop_first(df: pd.DataFrame, drop_features: List[str]) -> pd.DataFrame:
    return df.drop(columns=drop_features, errors="ignore")
