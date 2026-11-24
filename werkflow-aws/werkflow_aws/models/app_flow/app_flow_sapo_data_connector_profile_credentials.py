from __future__ import annotations
from pydantic import BaseModel
from .app_flow_basic_auth_credentials import AppFlowBasicAuthCredentials
from .app_flow_o_auth_credentials import AppFlowOAuthCredentials


class AppFlowSAPODataConnectorProfileCredentials(BaseModel):
    basicAuthCredentials: AppFlowBasicAuthCredentials | None = None
    oAuthCredentials: AppFlowOAuthCredentials | None = None
