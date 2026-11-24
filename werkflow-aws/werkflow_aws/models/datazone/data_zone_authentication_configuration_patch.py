from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_basic_authentication_credentials import DataZoneBasicAuthenticationCredentials
from .data_zone_o_auth2_properties_patch import DataZoneOAuth2PropertiesPatch


class DataZoneAuthenticationConfigurationPatch(BaseModel):
    secretArn: StrictStr | None = None
    basicAuthenticationCredentials: DataZoneBasicAuthenticationCredentials | None = None
    oAuth2Properties: DataZoneOAuth2PropertiesPatch | None = None
