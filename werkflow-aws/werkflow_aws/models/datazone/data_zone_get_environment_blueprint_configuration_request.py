from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGetEnvironmentBlueprintConfigurationRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentBlueprintIdentifier: StrictStr
