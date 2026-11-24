from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxDataRepositoryTaskFilter(BaseModel):
    Name: Literal['file-system-id', 'task-lifecycle', 'data-repository-association-id', 'file-cache-id'] | None = None
    Values: list[StrictStr] | None = None
