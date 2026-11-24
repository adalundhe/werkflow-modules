from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .api_gateway_v2_routing_rule_action import APIGatewayV2RoutingRuleAction
from .api_gateway_v2_routing_rule_condition import APIGatewayV2RoutingRuleCondition


class APIGatewayV2CreateRoutingRuleRequest(BaseModel):
    Actions: list[APIGatewayV2RoutingRuleAction]
    Conditions: list[APIGatewayV2RoutingRuleCondition]
    DomainName: StrictStr
    Priority: StrictInt
    DomainNameId: StrictStr | None = None
