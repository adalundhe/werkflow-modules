from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_portal_summary import APIGatewayV2PortalSummary


class APIGatewayV2ListPortalsResponse(BaseModel):
    Items: list[APIGatewayV2PortalSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
