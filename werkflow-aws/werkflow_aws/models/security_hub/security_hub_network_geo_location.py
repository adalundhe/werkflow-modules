from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class SecurityHubNetworkGeoLocation(BaseModel):
    City: StrictStr | None = None
    Country: StrictStr | None = None
    Lat: StrictFloat | StrictInt | None = None
    Lon: StrictFloat | StrictInt | None = None
