from __future__ import annotations
from typing import Literal


EC2SSEType = Literal[
    "sse-ebs",
    "sse-kms",
    "none",
]
