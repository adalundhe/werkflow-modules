from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_environment_parameter import DataZoneEnvironmentParameter


class DataZoneUpdateEnvironmentRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    glossaryTerms: list[StrictStr] | None = None
    blueprintVersion: StrictStr | None = None
    userParameters: list[DataZoneEnvironmentParameter] | None = None
    environmentConfigurationName: StrictStr | None = None
