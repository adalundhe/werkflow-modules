from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteEnvironmentActionRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentIdentifier: StrictStr
    identifier: StrictStr
