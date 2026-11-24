from __future__ import annotations
from typing import Literal


EKSClusterStatus = Literal[
    'CREATING',
    'ACTIVE',
    'DELETING',
    'FAILED',
    'UPDATING',
    'PENDING',
]
