from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyEnrichment(BaseModel):
    CountryName: StrictStr | None = None
    AsnOrg: StrictStr | None = None
    ThreatListName: StrictStr | None = None
    ThreatName: StrictStr | None = None
