# Python Package Deployment Example

## Overview

This code is meant to serve as an example of developing a pip-installable machine learning library that can be used for 
real-time inference by a deployed python package or another interoperable language.

This package demonstrates an ability to:
* Save model weights and include them in the python package for use after installation
* Use test driven development (TDD) to avoid scope creep and keep functions simple and maintainable
* Use node/pipeline architecture to simplify code execution when in production
* Use configs to handle variables that are likely to change over time for ease of finding and maintaining
* Design and implement a one-hot-encoding system that is reproducible even when specific categorical features are not present

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

