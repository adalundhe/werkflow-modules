from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LocationListRouteCalculatorsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
