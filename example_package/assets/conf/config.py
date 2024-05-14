def load_config():
    return {
        "FEATURES": ['bedrooms', 'bathrooms', 'area', 'basement', 'furnishingstatus'],
        "CATEGORICAL_FEATURES": ['basement', 'furnishingstatus'],
        "TARGET_VARIABLE": 'price'
    }
