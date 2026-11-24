from __future__ import annotations
from typing import Literal


RDSActivityStreamPolicyStatus = Literal[
    'locked',
    'unlocked',
    'locking-policy',
    'unlocking-policy',
]
