from __future__ import annotations
from typing import Literal


SageMakerRoutingStrategy = Literal[
    'LEAST_OUTSTANDING_REQUESTS',
    'RANDOM',
    'PREFIX_AWARE',
    'KV_AWARE',
]
