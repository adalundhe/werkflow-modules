from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2DeleteTransitGatewayMeteringPolicyEntryRequest(BaseModel):
    TransitGatewayMeteringPolicyId: StrictStr
    PolicyRuleNumber: StrictInt
    DryRun: StrictBool | None = None
