from __future__ import annotations
from typing import Literal


EKSFargateProfileStatus = Literal[
    'CREATING',
    'ACTIVE',
    'DELETING',
    'CREATE_FAILED',
    'DELETE_FAILED',
]
