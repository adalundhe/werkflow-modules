from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ListGeoLocationsRequest(BaseModel):
    StartContinentCode: StrictStr | None = None
    StartCountryCode: StrictStr | None = None
    StartSubdivisionCode: StrictStr | None = None
    MaxItems: StrictStr | None = None
