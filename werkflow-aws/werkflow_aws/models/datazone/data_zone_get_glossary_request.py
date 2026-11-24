from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetGlossaryRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
