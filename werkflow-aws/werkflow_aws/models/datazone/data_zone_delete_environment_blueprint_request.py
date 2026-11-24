from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteEnvironmentBlueprintRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
