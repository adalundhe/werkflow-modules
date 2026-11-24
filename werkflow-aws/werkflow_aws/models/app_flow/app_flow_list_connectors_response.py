from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_flow_connector_detail import AppFlowConnectorDetail


class AppFlowListConnectorsResponse(BaseModel):
    connectors: list[AppFlowConnectorDetail] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
