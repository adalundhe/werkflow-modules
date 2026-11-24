from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TaxSettingsJurisdiction(BaseModel):
    stateOrRegion: StrictStr | None = None
    countryCode: StrictStr | None = None
