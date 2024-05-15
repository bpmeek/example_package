# Python Package Deployment Example

## Overview

This code is meant to serve as an example of developing a pip-installable machine learning library that can be used for 
real-time inference by a deployed python package or another interoperable language.


## How to use

### Installation
After forking the repository and downloading locally:

Install build

`pip install build`

From the repo root, build wheel file

`python -m build`

.whl file will be built in the `dist/` folder and can be installed by running:

`pip install <path_to_whl>`

### In code

```python
>>> from example_package import Model
>>> model = Model()
>>> test = {
...     "bedrooms": 4,
...     "bathrooms": 2,
...     "area": 7420,
...     "basement": "no",
...     "furnishingstatus": "furnished"
... }
>>> model.predict(test)
array([7094687.53284395])
```

