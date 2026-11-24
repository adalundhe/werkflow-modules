from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .api_gateway_v2_routing_rule_action import APIGatewayV2RoutingRuleAction
from .api_gateway_v2_routing_rule_condition import APIGatewayV2RoutingRuleCondition


class APIGatewayV2RoutingRule(BaseModel):
    Actions: list[APIGatewayV2RoutingRuleAction] | None = None
    Conditions: list[APIGatewayV2RoutingRuleCondition] | None = None
    Priority: StrictInt | None = None
    RoutingRuleArn: StrictStr | None = None
    RoutingRuleId: StrictStr | None = None
