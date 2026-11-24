from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .data_zone_environment_parameter import DataZoneEnvironmentParameter


class DataZoneCreateEnvironmentRequest(BaseModel):
    projectIdentifier: StrictStr
    domainIdentifier: StrictStr
    name: StrictStr
    description: StrictStr | None = None
    environmentProfileIdentifier: StrictStr | None = None
    userParameters: list[DataZoneEnvironmentParameter] | None = None
    glossaryTerms: list[StrictStr] | None = None
    environmentAccountIdentifier: StrictStr | None = None
    environmentAccountRegion: StrictStr | None = None
    environmentBlueprintIdentifier: StrictStr | None = None
    deploymentOrder: StrictInt | None = None
    environmentConfigurationId: StrictStr | None = None
    environmentConfigurationName: StrictStr | None = None
