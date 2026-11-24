from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_provisioning_configuration import DataZoneProvisioningConfiguration
from .data_zone_resource_configuration import DataZoneResourceConfiguration


class DataZoneGetEnvironmentBlueprintConfigurationResponse(BaseModel):
    domainId: StrictStr | None = None
    environmentBlueprintId: StrictStr | None = None
    provisioningRoleArn: StrictStr | None = None
    environmentRolePermissionBoundary: StrictStr | None = None
    manageAccessRoleArn: StrictStr | None = None
    enabledRegions: list[StrictStr] | None = None
    regionalParameters: dict[StrictStr, dict[StrictStr, StrictStr]] | None = None
    allowUserProvidedConfigurations: StrictBool | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    resourceConfigurations: list[DataZoneResourceConfiguration] | None = None
    provisioningConfigurations: list[DataZoneProvisioningConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
