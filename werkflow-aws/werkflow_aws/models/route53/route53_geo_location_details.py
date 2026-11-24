from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53GeoLocationDetails(BaseModel):
    ContinentCode: StrictStr | None = None
    ContinentName: StrictStr | None = None
    CountryCode: StrictStr | None = None
    CountryName: StrictStr | None = None
    SubdivisionCode: StrictStr | None = None
    SubdivisionName: StrictStr | None = None
