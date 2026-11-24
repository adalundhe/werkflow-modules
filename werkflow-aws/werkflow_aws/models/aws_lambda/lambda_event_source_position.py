from __future__ import annotations
from typing import Literal


LambdaEventSourcePosition = Literal[
    'TRIM_HORIZON',
    'LATEST',
    'AT_TIMESTAMP',
]
