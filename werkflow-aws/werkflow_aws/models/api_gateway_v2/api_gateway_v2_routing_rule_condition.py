from __future__ import annotations
from pydantic import BaseModel
from .api_gateway_v2_routing_rule_match_base_paths import APIGatewayV2RoutingRuleMatchBasePaths
from .api_gateway_v2_routing_rule_match_headers import APIGatewayV2RoutingRuleMatchHeaders


class APIGatewayV2RoutingRuleCondition(BaseModel):
    MatchBasePaths: APIGatewayV2RoutingRuleMatchBasePaths | None = None
    MatchHeaders: APIGatewayV2RoutingRuleMatchHeaders | None = None
