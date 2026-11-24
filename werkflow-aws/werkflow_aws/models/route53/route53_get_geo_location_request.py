from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53GetGeoLocationRequest(BaseModel):
    ContinentCode: StrictStr | None = None
    CountryCode: StrictStr | None = None
    SubdivisionCode: StrictStr | None = None
