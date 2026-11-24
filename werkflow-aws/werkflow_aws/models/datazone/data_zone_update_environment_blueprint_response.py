from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_custom_parameter import DataZoneCustomParameter
from .data_zone_deployment_properties import DataZoneDeploymentProperties
from .data_zone_provisioning_properties import DataZoneProvisioningProperties


class DataZoneUpdateEnvironmentBlueprintResponse(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    provider: StrictStr | None = None
    provisioningProperties: DataZoneProvisioningProperties | None = None
    deploymentProperties: DataZoneDeploymentProperties | None = None
    userParameters: list[DataZoneCustomParameter] | None = None
    glossaryTerms: list[StrictStr] | None = None
    blueprintCategory: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
