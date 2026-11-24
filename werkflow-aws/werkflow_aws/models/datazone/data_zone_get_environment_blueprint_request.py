from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetEnvironmentBlueprintRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
