from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class FSxS3AccessPointAttachmentsFilter(BaseModel):
    Name: Literal['file-system-id', 'volume-id', 'type'] | None = None
    Values: list[StrictStr] | None = None
