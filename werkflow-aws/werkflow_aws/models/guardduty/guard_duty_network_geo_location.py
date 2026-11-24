from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GuardDutyNetworkGeoLocation(BaseModel):
    City: StrictStr | None = None
    Country: StrictStr | None = None
    Latitude: StrictFloat | StrictInt | None = None
    Longitude: StrictFloat | StrictInt | None = None
