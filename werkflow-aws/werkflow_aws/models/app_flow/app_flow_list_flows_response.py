from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_flow_flow_definition import AppFlowFlowDefinition


class AppFlowListFlowsResponse(BaseModel):
    flows: list[AppFlowFlowDefinition] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
