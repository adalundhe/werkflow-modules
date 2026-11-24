from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_environment_configuration_user_parameter import DataZoneEnvironmentConfigurationUserParameter
from .data_zone_environment_deployment_details import DataZoneEnvironmentDeploymentDetails
from .data_zone_project_deletion_error import DataZoneProjectDeletionError
from .data_zone_resource_tag import DataZoneResourceTag


class DataZoneCreateProjectResponse(BaseModel):
    domainId: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    projectStatus: StrictStr | None = None
    failureReasons: list[DataZoneProjectDeletionError] | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    lastUpdatedAt: datetime.datetime | StrictStr | None = None
    resourceTags: list[DataZoneResourceTag] | None = None
    glossaryTerms: list[StrictStr] | None = None
    domainUnitId: StrictStr | None = None
    projectProfileId: StrictStr | None = None
    userParameters: list[DataZoneEnvironmentConfigurationUserParameter] | None = None
    environmentDeploymentDetails: DataZoneEnvironmentDeploymentDetails | None = None
    projectCategory: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
