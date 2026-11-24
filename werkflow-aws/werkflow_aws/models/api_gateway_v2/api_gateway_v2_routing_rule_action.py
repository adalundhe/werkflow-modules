from __future__ import annotations
from pydantic import BaseModel
from .api_gateway_v2_routing_rule_action_invoke_api import APIGatewayV2RoutingRuleActionInvokeApi


class APIGatewayV2RoutingRuleAction(BaseModel):
    InvokeApi: APIGatewayV2RoutingRuleActionInvokeApi | None = None
