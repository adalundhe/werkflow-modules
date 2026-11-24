from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_connector_o_auth_request import AppFlowConnectorOAuthRequest


class AppFlowOAuth2Credentials(BaseModel):
    clientId: StrictStr | None = None
    clientSecret: StrictStr | None = None
    accessToken: StrictStr | None = None
    refreshToken: StrictStr | None = None
    oAuthRequest: AppFlowConnectorOAuthRequest | None = None
