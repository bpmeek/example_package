# Python Package Deployment Example

## Overview

This code is meant to serve as an example of developing a pip-installable machine learning library that can be used for 
real-time inference by a deployed python package or another interoperable language.


## How to use

### Installation

### In code
```python
from example_package import Model
model = Model()
test = {
    "bedrooms": 4,
    "bathrooms": 2,
    "area": 7420,
    "basement": "no",
    "furnishingstatus": "furnished"
}
model.predict(test)
```