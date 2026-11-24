from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationDeleteMapRequest(BaseModel):
    MapName: StrictStr
