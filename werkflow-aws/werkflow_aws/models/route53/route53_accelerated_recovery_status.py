from __future__ import annotations
from typing import Literal


Route53AcceleratedRecoveryStatus = Literal[
    'ENABLING',
    'ENABLE_FAILED',
    'ENABLING_HOSTED_ZONE_LOCKED',
    'ENABLED',
    'DISABLING',
    'DISABLE_FAILED',
    'DISABLED',
    'DISABLING_HOSTED_ZONE_LOCKED',
]
