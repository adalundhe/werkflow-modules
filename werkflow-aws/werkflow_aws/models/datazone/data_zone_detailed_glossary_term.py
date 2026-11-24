from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDetailedGlossaryTerm(BaseModel):
    name: StrictStr | None = None
    shortDescription: StrictStr | None = None
