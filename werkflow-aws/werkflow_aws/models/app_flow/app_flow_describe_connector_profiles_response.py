from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .app_flow_connector_profile import AppFlowConnectorProfile


class AppFlowDescribeConnectorProfilesResponse(BaseModel):
    connectorProfileDetails: list[AppFlowConnectorProfile] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
