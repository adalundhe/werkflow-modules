from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSGatewayRouteLoadBalancerSecurityGroup(BaseModel):
    arn: StrictStr | None = None
    ruleArns: list[StrictStr] | None = None
