from __future__ import annotations
from typing import Literal


Route53ComparisonOperator = Literal[
    'GreaterThanOrEqualToThreshold',
    'GreaterThanThreshold',
    'LessThanThreshold',
    'LessThanOrEqualToThreshold',
]
