from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_basic_authentication_credentials import DataZoneBasicAuthenticationCredentials
from .data_zone_o_auth2_properties import DataZoneOAuth2Properties


class DataZoneAuthenticationConfigurationInput(BaseModel):
    authenticationType: Literal['BASIC', 'OAUTH2', 'CUSTOM'] | None = None
    oAuth2Properties: DataZoneOAuth2Properties | None = None
    secretArn: StrictStr | None = None
    kmsKeyArn: StrictStr | None = None
    basicAuthenticationCredentials: DataZoneBasicAuthenticationCredentials | None = None
    customAuthenticationCredentials: dict[StrictStr, StrictStr] | None = None
