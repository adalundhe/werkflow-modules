from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .app_flow_api_key_credentials import AppFlowApiKeyCredentials
from .app_flow_basic_auth_credentials import AppFlowBasicAuthCredentials
from .app_flow_custom_auth_credentials import AppFlowCustomAuthCredentials
from .app_flow_o_auth2_credentials import AppFlowOAuth2Credentials


class AppFlowCustomConnectorProfileCredentials(BaseModel):
    authenticationType: Literal['OAUTH2', 'APIKEY', 'BASIC', 'CUSTOM']
    basic: AppFlowBasicAuthCredentials | None = None
    oauth2: AppFlowOAuth2Credentials | None = None
    apiKey: AppFlowApiKeyCredentials | None = None
    custom: AppFlowCustomAuthCredentials | None = None
