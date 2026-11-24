from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_flow_connector_configuration import AppFlowConnectorConfiguration


class AppFlowDescribeConnectorResponse(BaseModel):
    connectorConfiguration: AppFlowConnectorConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
