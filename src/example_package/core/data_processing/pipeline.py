import pandas as pd

from typing import Dict, Any, List

from .functions import check_dataframe, encode, drop_first


def process_data(
        data: pd.DataFrame or Dict[str, Any], categorical_features: List[str], drop_features: List[str]
) -> pd.DataFrame:
    df = check_dataframe(data)
    encoded = encode(df, categorical_features)
    dropped = drop_first(encoded, drop_features)
    return dropped
