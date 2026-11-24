from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationDescribeGeofenceCollectionRequest(BaseModel):
    CollectionName: StrictStr
