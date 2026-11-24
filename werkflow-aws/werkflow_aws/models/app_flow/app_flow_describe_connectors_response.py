from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_flow_connector_configuration import AppFlowConnectorConfiguration
from .app_flow_connector_detail import AppFlowConnectorDetail


class AppFlowDescribeConnectorsResponse(BaseModel):
    connectorConfigurations: dict[StrictStr, AppFlowConnectorConfiguration] | None = None
    connectors: list[AppFlowConnectorDetail] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
