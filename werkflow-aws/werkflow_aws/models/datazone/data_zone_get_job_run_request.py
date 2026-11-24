from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetJobRunRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
