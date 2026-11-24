from __future__ import annotations
from typing import Literal


RDSWriteForwardingStatus = Literal[
    'enabled',
    'disabled',
    'enabling',
    'disabling',
    'unknown',
]
