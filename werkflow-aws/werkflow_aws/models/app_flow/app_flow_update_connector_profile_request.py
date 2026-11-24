from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_flow_connector_profile_config import AppFlowConnectorProfileConfig


class AppFlowUpdateConnectorProfileRequest(BaseModel):
    connectorProfileName: StrictStr
    connectionMode: Literal['Public', 'Private']
    connectorProfileConfig: AppFlowConnectorProfileConfig
    clientToken: StrictStr | None = None
