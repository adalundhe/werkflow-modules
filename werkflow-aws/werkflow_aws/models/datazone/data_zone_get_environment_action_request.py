from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetEnvironmentActionRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
    identifier: StrictStr
