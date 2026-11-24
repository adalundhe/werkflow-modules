from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxSnapshotFilter(BaseModel):
    Name: Literal['file-system-id', 'volume-id'] | None = None
    Values: list[StrictStr] | None = None
