from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_usage_plan_key import APIGatewayUsagePlanKey


class APIGatewayGetUsagePlanKeysResponse(BaseModel):
    position: StrictStr | None = None
    items: list[APIGatewayUsagePlanKey] | None = None
    ResponseMetadata: dict[str, Any] | None = None
