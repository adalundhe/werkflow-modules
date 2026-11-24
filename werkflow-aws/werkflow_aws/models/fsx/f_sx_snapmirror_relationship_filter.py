from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxSnapmirrorRelationshipFilter(BaseModel):
    Name: Literal['file-system-id', 'destination-volume-id'] | None = None
    Values: list[StrictStr] | None = None
