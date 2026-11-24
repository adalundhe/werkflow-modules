from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_o_auth2_credentials import AppFlowOAuth2Credentials


class AppFlowServiceNowConnectorProfileCredentials(BaseModel):
    username: StrictStr | None = None
    password: StrictStr | None = None
    oAuth2Credentials: AppFlowOAuth2Credentials | None = None
