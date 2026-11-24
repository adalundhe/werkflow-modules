from __future__ import annotations
from pydantic import BaseModel
from .app_flow_connector_profile_credentials import AppFlowConnectorProfileCredentials
from .app_flow_connector_profile_properties import AppFlowConnectorProfileProperties


class AppFlowConnectorProfileConfig(BaseModel):
    connectorProfileProperties: AppFlowConnectorProfileProperties
    connectorProfileCredentials: AppFlowConnectorProfileCredentials | None = None
