from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationDescribeMapRequest(BaseModel):
    MapName: StrictStr
