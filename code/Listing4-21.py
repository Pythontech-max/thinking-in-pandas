import io

import pandas as pd


data = io.StringIO(
"""
[{"location": "234unf923", "temp": 35.2}, {"location": "340inf351", "temp": 32.5}, {"location": "234abe045", "temp": 33.1}]
"""
)

print(pd.read_json(data, orient="records"))
