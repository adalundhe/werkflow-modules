from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .app_flow_custom_auth_config import AppFlowCustomAuthConfig
from .app_flow_o_auth2_defaults import AppFlowOAuth2Defaults


class AppFlowAuthenticationConfig(BaseModel):
    isBasicAuthSupported: StrictBool | None = None
    isApiKeyAuthSupported: StrictBool | None = None
    isOAuth2Supported: StrictBool | None = None
    isCustomAuthSupported: StrictBool | None = None
    oAuth2Defaults: AppFlowOAuth2Defaults | None = None
    customAuthConfigs: list[AppFlowCustomAuthConfig] | None = None
