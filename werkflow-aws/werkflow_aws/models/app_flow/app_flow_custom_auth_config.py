from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_auth_parameter import AppFlowAuthParameter


class AppFlowCustomAuthConfig(BaseModel):
    customAuthenticationType: StrictStr | None = None
    authParameters: list[AppFlowAuthParameter] | None = None
