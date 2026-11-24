from __future__ import annotations
from typing import Literal


EKSAddonStatus = Literal[
    'CREATING',
    'ACTIVE',
    'CREATE_FAILED',
    'UPDATING',
    'DELETING',
    'DELETE_FAILED',
    'DEGRADED',
    'UPDATE_FAILED',
]
