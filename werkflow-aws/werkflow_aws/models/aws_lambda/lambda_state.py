from __future__ import annotations
from typing import Literal


LambdaState = Literal[
    'Pending',
    'Active',
    'Inactive',
    'Failed',
    'Deactivating',
    'Deactivated',
    'ActiveNonInvocable',
    'Deleting',
]
