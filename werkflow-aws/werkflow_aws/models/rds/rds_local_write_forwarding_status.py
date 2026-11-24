from __future__ import annotations
from typing import Literal


RDSLocalWriteForwardingStatus = Literal[
    'enabled',
    'disabled',
    'enabling',
    'disabling',
    'requested',
]
