from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationDeleteGeofenceCollectionRequest(BaseModel):
    CollectionName: StrictStr
