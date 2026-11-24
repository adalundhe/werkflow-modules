from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_usage_plan import APIGatewayUsagePlan


class APIGatewayGetUsagePlansResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayUsagePlan] | None = None
    ResponseMetadata: dict[str, Any] | None = None
