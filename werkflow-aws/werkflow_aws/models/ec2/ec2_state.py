from __future__ import annotations
from typing import Literal


EC2State = Literal[
    "creating",
    "available",
    "in-use",
    "deleting",
    "deleted",
    "error",
]
