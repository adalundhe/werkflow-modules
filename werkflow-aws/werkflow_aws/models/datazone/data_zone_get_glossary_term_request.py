from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetGlossaryTermRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
