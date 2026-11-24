from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_authentication_configuration_patch import DataZoneAuthenticationConfigurationPatch


class DataZoneConnectivityPropertiesPatch(BaseModel):
    description: StrictStr | None = None
    connectionProperties: dict[StrictStr, StrictStr] | None = None
    authenticationConfiguration: DataZoneAuthenticationConfigurationPatch | None = None
