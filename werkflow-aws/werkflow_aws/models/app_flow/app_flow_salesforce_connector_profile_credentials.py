from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_flow_connector_o_auth_request import AppFlowConnectorOAuthRequest


class AppFlowSalesforceConnectorProfileCredentials(BaseModel):
    accessToken: StrictStr | None = None
    refreshToken: StrictStr | None = None
    oAuthRequest: AppFlowConnectorOAuthRequest | None = None
    clientCredentialsArn: StrictStr | None = None
    oAuth2GrantType: Literal['CLIENT_CREDENTIALS', 'AUTHORIZATION_CODE', 'JWT_BEARER'] | None = None
    jwtToken: StrictStr | None = None
