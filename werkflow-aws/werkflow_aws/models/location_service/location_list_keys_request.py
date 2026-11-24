from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .location_api_key_filter import LocationApiKeyFilter


class LocationListKeysRequest(BaseModel):
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    Filter: LocationApiKeyFilter | None = None
