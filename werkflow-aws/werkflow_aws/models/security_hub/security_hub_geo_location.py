from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class SecurityHubGeoLocation(BaseModel):
    Lon: StrictFloat | StrictInt | None = None
    Lat: StrictFloat | StrictInt | None = None
