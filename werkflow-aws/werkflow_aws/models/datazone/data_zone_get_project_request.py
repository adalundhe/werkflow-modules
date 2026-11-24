from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetProjectRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
