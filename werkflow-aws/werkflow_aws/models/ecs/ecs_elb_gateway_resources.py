from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSElbGatewayResources(BaseModel):
    loadBalancerArn: StrictStr | None = None
    listenerArn: StrictStr | None = None
    securityGroup: StrictStr | None = None
    gatewayRouteArns: list[StrictStr] | None = None
