from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_o_auth2_properties import AppFlowOAuth2Properties


class AppFlowCustomConnectorProfileProperties(BaseModel):
    profileProperties: dict[StrictStr, StrictStr] | None = None
    oAuth2Properties: AppFlowOAuth2Properties | None = None
