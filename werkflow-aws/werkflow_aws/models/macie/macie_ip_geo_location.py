from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class MacieIpGeoLocation(BaseModel):
    lat: StrictFloat | StrictInt | None = None
    lon: StrictFloat | StrictInt | None = None
