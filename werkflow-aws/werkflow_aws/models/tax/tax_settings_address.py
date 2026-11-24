from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsAddress(BaseModel):
    addressLine1: StrictStr | None = None
    addressLine2: StrictStr | None = None
    addressLine3: StrictStr | None = None
    districtOrCounty: StrictStr | None = None
    city: StrictStr | None = None
    stateOrRegion: StrictStr | None = None
    postalCode: StrictStr | None = None
    countryCode: StrictStr | None = None
