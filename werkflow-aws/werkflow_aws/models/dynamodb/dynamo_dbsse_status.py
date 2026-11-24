from __future__ import annotations
from typing import Literal


DynamoDBSSEStatus = Literal[
    'ENABLING',
    'ENABLED',
    'DISABLING',
    'DISABLED',
    'UPDATING',
]
