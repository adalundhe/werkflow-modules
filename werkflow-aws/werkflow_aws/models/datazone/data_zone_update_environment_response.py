from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_configurable_environment_action import DataZoneConfigurableEnvironmentAction
from .data_zone_custom_parameter import DataZoneCustomParameter
from .data_zone_deployment import DataZoneDeployment
from .data_zone_deployment_properties import DataZoneDeploymentProperties
from .data_zone_provisioning_properties import DataZoneProvisioningProperties
from .data_zone_resource import DataZoneResource


class DataZoneUpdateEnvironmentResponse(BaseModel):
    projectId: StrictStr | None = None
    id: StrictStr | None = None
    domainId: StrictStr | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    environmentProfileId: StrictStr | None = None
    awsAccountId: StrictStr | None = None
    awsAccountRegion: StrictStr | None = None
    provider: StrictStr | None = None
    provisionedResources: list[DataZoneResource] | None = None
    status: StrictStr | None = None
    environmentActions: list[DataZoneConfigurableEnvironmentAction] | None = None
    glossaryTerms: list[StrictStr] | None = None
    userParameters: list[DataZoneCustomParameter] | None = None
    lastDeployment: DataZoneDeployment | None = None
    provisioningProperties: DataZoneProvisioningProperties | None = None
    deploymentProperties: DataZoneDeploymentProperties | None = None
    environmentBlueprintId: StrictStr | None = None
    environmentConfigurationId: StrictStr | None = None
    environmentConfigurationName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
