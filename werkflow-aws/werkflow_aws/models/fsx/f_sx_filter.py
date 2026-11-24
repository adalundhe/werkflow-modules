from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxFilter(BaseModel):
    Name: Literal['file-system-id', 'backup-type', 'file-system-type', 'volume-id', 'data-repository-type', 'file-cache-id', 'file-cache-type'] | None = None
    Values: list[StrictStr] | None = None
