from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_o_auth2_client_application import DataZoneOAuth2ClientApplication


class DataZoneOAuth2PropertiesPatch(BaseModel):
    oAuth2GrantType: Literal['AUTHORIZATION_CODE', 'CLIENT_CREDENTIALS', 'JWT_BEARER'] | None = None
    oAuth2ClientApplication: DataZoneOAuth2ClientApplication | None = None
    tokenUrl: StrictStr | None = None
    tokenUrlParametersMap: dict[StrictStr, StrictStr] | None = None
