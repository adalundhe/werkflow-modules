from __future__ import annotations
from typing import Literal


EC2VolumeType = Literal[
    "standard",
    "io1",
    "io2",
    "gp2",
    "sc1",
    "st1",
    "gp3",
]
