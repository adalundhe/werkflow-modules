from __future__ import annotations
from pydantic import BaseModel
from .api_gateway_v2_routing_rule_match_header_value import APIGatewayV2RoutingRuleMatchHeaderValue


class APIGatewayV2RoutingRuleMatchHeaders(BaseModel):
    AnyOf: list[APIGatewayV2RoutingRuleMatchHeaderValue] | None = None
