from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSGatewayConnectionAlbResources(BaseModel):
    acmCertificateArn: StrictStr | None = None
    loadBalancerArn: StrictStr | None = None
    loadBalancerSecurityGroupArns: list[StrictStr] | None = None
    listenerArn: StrictStr | None = None
    listenerRuleArn: StrictStr | None = None
    testListenerRuleArn: StrictStr | None = None
    targetGroupArn: StrictStr | None = None
    alternateTargetGroupArn: StrictStr | None = None
