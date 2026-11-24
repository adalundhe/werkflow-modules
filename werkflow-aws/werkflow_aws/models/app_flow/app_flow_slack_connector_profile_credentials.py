from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_connector_o_auth_request import AppFlowConnectorOAuthRequest


class AppFlowSlackConnectorProfileCredentials(BaseModel):
    clientId: StrictStr
    clientSecret: StrictStr
    accessToken: StrictStr | None = None
    oAuthRequest: AppFlowConnectorOAuthRequest | None = None
