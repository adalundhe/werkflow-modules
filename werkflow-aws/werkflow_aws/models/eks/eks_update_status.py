from __future__ import annotations
from typing import Literal


EKSUpdateStatus = Literal[
    'InProgress',
    'Failed',
    'Cancelled',
    'Successful',
]
