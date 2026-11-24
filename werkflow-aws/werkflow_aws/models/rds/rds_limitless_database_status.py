from __future__ import annotations
from typing import Literal


RDSLimitlessDatabaseStatus = Literal[
    'active',
    'not-in-use',
    'enabled',
    'disabled',
    'enabling',
    'disabling',
    'modifying-max-capacity',
    'error',
]
