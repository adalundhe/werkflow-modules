from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_flow_connector_entity import AppFlowConnectorEntity


class AppFlowListConnectorEntitiesResponse(BaseModel):
    connectorEntityMap: dict[StrictStr, list[AppFlowConnectorEntity]] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
