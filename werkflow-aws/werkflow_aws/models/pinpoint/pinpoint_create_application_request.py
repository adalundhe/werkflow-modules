from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointCreateApplicationRequest(BaseModel):
    Name: StrictStr
    tags: dict[StrictStr, StrictStr] | None = None
