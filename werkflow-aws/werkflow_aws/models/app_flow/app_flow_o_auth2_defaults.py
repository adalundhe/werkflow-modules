from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_o_auth2_custom_parameter import AppFlowOAuth2CustomParameter


class AppFlowOAuth2Defaults(BaseModel):
    oauthScopes: list[StrictStr] | None = None
    tokenUrls: list[StrictStr] | None = None
    authCodeUrls: list[StrictStr] | None = None
    oauth2GrantTypesSupported: list[StrictStr] | None = None
    oauth2CustomProperties: list[AppFlowOAuth2CustomParameter] | None = None
