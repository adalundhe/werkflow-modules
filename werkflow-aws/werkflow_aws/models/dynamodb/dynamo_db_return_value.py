from __future__ import annotations
from typing import Literal


DynamoDBReturnValue = Literal[
    'NONE',
    'ALL_OLD',
    'UPDATED_OLD',
    'ALL_NEW',
    'UPDATED_NEW',
]
