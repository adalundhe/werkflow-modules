from __future__ import annotations
from typing import Literal


DynamoDBTimeToLiveStatus = Literal[
    'ENABLING',
    'DISABLING',
    'ENABLED',
    'DISABLED',
]
