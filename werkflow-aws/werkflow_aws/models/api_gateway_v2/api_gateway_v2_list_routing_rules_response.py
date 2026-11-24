from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .api_gateway_v2_routing_rule import APIGatewayV2RoutingRule


class APIGatewayV2ListRoutingRulesResponse(BaseModel):
    NextToken: StrictStr | None = None
    RoutingRules: list[APIGatewayV2RoutingRule] | None = None
    ResponseMetadata: dict[str, Any] | None = None
