from __future__ import annotations
from typing import Literal


DynamoDBTableStatus = Literal[
    'CREATING',
    'UPDATING',
    'DELETING',
    'ACTIVE',
    'INACCESSIBLE_ENCRYPTION_CREDENTIALS',
    'ARCHIVING',
    'ARCHIVED',
    'REPLICATION_NOT_AUTHORIZED',
]
