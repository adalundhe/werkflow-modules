from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_o_auth2_properties import DataZoneOAuth2Properties


class DataZoneAuthenticationConfiguration(BaseModel):
    authenticationType: StrictStr | None = None
    secretArn: StrictStr | None = None
    oAuth2Properties: DataZoneOAuth2Properties | None = None
