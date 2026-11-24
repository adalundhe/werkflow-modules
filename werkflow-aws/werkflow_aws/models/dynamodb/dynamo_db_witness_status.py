from __future__ import annotations
from typing import Literal


DynamoDBWitnessStatus = Literal[
    'CREATING',
    'DELETING',
    'ACTIVE',
]
