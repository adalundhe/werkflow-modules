from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class LocationDeleteKeyRequest(BaseModel):
    KeyName: StrictStr
    ForceDelete: StrictBool | None = None
