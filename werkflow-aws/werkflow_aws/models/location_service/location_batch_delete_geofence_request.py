from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationBatchDeleteGeofenceRequest(BaseModel):
    CollectionName: StrictStr
    GeofenceIds: list[StrictStr]
