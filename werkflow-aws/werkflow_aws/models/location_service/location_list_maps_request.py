from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LocationListMapsRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
