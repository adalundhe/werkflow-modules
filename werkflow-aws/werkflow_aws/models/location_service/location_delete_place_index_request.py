from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationDeletePlaceIndexRequest(BaseModel):
    IndexName: StrictStr
