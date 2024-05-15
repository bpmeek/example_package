def load_config():
    return {
        "DROP_FEATURES": ["basement_no", "furnishingstatus_furnished"],
        "CATEGORICAL_FEATURES": ["basement_yes", "furnishingstatus_semi-furnished", "furnishingstatus_unfurnished"],
        "TARGET_VARIABLE": 'price'
    }
