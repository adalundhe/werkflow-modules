from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_environment_parameter import DataZoneEnvironmentParameter


class DataZoneCreateEnvironmentProfileRequest(BaseModel):
    domainIdentifier: StrictStr
    name: StrictStr
    environmentBlueprintIdentifier: StrictStr
    projectIdentifier: StrictStr
    description: StrictStr | None = None
    userParameters: list[DataZoneEnvironmentParameter] | None = None
    awsAccountId: StrictStr | None = None
    awsAccountRegion: StrictStr | None = None
