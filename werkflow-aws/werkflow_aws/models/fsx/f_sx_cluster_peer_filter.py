from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxClusterPeerFilter(BaseModel):
    Name: Literal['file-system-id'] | None = None
    Values: list[StrictStr] | None = None
