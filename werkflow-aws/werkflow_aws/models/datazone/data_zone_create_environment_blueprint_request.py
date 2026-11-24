from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_custom_parameter import DataZoneCustomParameter
from .data_zone_provisioning_properties import DataZoneProvisioningProperties


class DataZoneCreateEnvironmentBlueprintRequest(BaseModel):
    domainIdentifier: StrictStr
    name: StrictStr
    provisioningProperties: DataZoneProvisioningProperties
    description: StrictStr | None = None
    userParameters: list[DataZoneCustomParameter] | None = None
    blueprintCategory: Literal['TOOLING'] | None = None
