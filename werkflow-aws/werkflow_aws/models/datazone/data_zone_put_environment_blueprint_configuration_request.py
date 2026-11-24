from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .data_zone_provisioning_configuration import DataZoneProvisioningConfiguration
from .data_zone_put_resource_configuration import DataZonePutResourceConfiguration


class DataZonePutEnvironmentBlueprintConfigurationRequest(BaseModel):
    domainIdentifier: StrictStr
    environmentBlueprintIdentifier: StrictStr
    enabledRegions: list[StrictStr]
    provisioningRoleArn: StrictStr | None = None
    manageAccessRoleArn: StrictStr | None = None
    environmentRolePermissionBoundary: StrictStr | None = None
    regionalParameters: dict[StrictStr, dict[StrictStr, StrictStr]] | None = None
    resourceConfigurations: list[DataZonePutResourceConfiguration] | None = None
    allowUserProvidedConfigurations: StrictBool | None = None
    globalParameters: dict[StrictStr, StrictStr] | None = None
    provisioningConfigurations: list[DataZoneProvisioningConfiguration] | None = None
