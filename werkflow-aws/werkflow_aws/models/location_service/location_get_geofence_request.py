from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationGetGeofenceRequest(BaseModel):
    CollectionName: StrictStr
    GeofenceId: StrictStr
