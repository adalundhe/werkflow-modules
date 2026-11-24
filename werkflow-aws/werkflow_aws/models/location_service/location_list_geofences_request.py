from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LocationListGeofencesRequest(BaseModel):
    CollectionName: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
