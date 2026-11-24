from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_environment_parameter import DataZoneEnvironmentParameter


class DataZoneUpdateEnvironmentProfileRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    userParameters: list[DataZoneEnvironmentParameter] | None = None
    awsAccountId: StrictStr | None = None
    awsAccountRegion: StrictStr | None = None
