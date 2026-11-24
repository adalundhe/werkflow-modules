from __future__ import annotations
from typing import Literal


DynamoDBIndexStatus = Literal[
    'CREATING',
    'UPDATING',
    'DELETING',
    'ACTIVE',
]
