from __future__ import annotations
from typing import Literal


EKSNodegroupStatus = Literal[
    'CREATING',
    'ACTIVE',
    'UPDATING',
    'DELETING',
    'CREATE_FAILED',
    'DELETE_FAILED',
    'DEGRADED',
]
