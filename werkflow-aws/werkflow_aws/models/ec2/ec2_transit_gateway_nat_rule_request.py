from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2TransitGatewayNatRuleRequest(BaseModel):
    RuleNumber: StrictInt | None = None
    MatchSourceCidr: StrictStr | None = None
    NatCidr: StrictStr | None = None
