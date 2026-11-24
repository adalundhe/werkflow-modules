from __future__ import annotations
from typing import Literal


DynamoDBComparisonOperator = Literal[
    'EQ',
    'NE',
    'IN',
    'LE',
    'LT',
    'GE',
    'GT',
    'BETWEEN',
    'NOT_NULL',
    'NULL',
    'CONTAINS',
    'NOT_CONTAINS',
    'BEGINS_WITH',
]
