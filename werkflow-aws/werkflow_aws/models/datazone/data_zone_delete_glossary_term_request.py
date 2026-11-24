from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteGlossaryTermRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
