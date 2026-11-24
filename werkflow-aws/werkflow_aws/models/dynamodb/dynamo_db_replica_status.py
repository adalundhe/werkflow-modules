from __future__ import annotations
from typing import Literal


DynamoDBReplicaStatus = Literal[
    'CREATING',
    'CREATION_FAILED',
    'UPDATING',
    'DELETING',
    'ACTIVE',
    'REGION_DISABLED',
    'INACCESSIBLE_ENCRYPTION_CREDENTIALS',
    'ARCHIVING',
    'ARCHIVED',
    'REPLICATION_NOT_AUTHORIZED',
]
