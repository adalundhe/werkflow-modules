from __future__ import annotations
from typing import Literal


DynamoDBStreamViewType = Literal[
    'NEW_IMAGE',
    'OLD_IMAGE',
    'NEW_AND_OLD_IMAGES',
    'KEYS_ONLY',
]
