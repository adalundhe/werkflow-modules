from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointUpdateAttributesRequest(BaseModel):
    Blacklist: list[StrictStr] | None = None
