from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_environment_configuration_user_parameter import DataZoneEnvironmentConfigurationUserParameter
from .data_zone_environment_deployment_details import DataZoneEnvironmentDeploymentDetails


class DataZoneUpdateProjectRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    name: StrictStr | None = None
    description: StrictStr | None = None
    resourceTags: dict[StrictStr, StrictStr] | None = None
    glossaryTerms: list[StrictStr] | None = None
    domainUnitId: StrictStr | None = None
    environmentDeploymentDetails: DataZoneEnvironmentDeploymentDetails | None = None
    userParameters: list[DataZoneEnvironmentConfigurationUserParameter] | None = None
    projectProfileVersion: StrictStr | None = None
    projectProfileAction: Literal['DISASSOCIATE'] | None = None
