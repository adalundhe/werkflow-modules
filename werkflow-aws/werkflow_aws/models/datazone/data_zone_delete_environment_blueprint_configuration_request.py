from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneDeleteEnvironmentBlueprintConfigurationRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentBlueprintIdentifier: StrictStr
