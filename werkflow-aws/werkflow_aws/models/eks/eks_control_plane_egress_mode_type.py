from __future__ import annotations
from typing import Literal


EKSControlPlaneEgressModeType = Literal[
    'AWS_MANAGED',
    'CUSTOMER_ROUTED',
    'CUSTOMER_ISOLATED',
]
