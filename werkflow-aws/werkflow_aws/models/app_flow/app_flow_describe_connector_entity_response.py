from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .app_flow_connector_entity_field import AppFlowConnectorEntityField


class AppFlowDescribeConnectorEntityResponse(BaseModel):
    connectorEntityFields: list[AppFlowConnectorEntityField] | None = None
    ResponseMetadata: dict[str, Any] | None = None
