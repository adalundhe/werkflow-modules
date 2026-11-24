from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_authorization_code_properties import DataZoneAuthorizationCodeProperties
from .data_zone_glue_o_auth2_credentials import DataZoneGlueOAuth2Credentials
from .data_zone_o_auth2_client_application import DataZoneOAuth2ClientApplication


class DataZoneOAuth2Properties(BaseModel):
    oAuth2GrantType: StrictStr | None = None
    oAuth2ClientApplication: DataZoneOAuth2ClientApplication | None = None
    tokenUrl: StrictStr | None = None
    tokenUrlParametersMap: dict[StrictStr, StrictStr] | None = None
    authorizationCodeProperties: DataZoneAuthorizationCodeProperties | None = None
    oAuth2Credentials: DataZoneGlueOAuth2Credentials | None = None
