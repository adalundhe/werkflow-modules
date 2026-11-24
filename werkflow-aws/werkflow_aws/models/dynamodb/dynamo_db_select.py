from __future__ import annotations
from typing import Literal


DynamoDBSelect = Literal[
    'ALL_ATTRIBUTES',
    'ALL_PROJECTED_ATTRIBUTES',
    'SPECIFIC_ATTRIBUTES',
    'COUNT',
]
