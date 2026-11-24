from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class PinpointEndpointLocation(BaseModel):
    City: StrictStr | None = None
    Country: StrictStr | None = None
    Latitude: StrictFloat | StrictInt | None = None
    Longitude: StrictFloat | StrictInt | None = None
    PostalCode: StrictStr | None = None
    Region: StrictStr | None = None
