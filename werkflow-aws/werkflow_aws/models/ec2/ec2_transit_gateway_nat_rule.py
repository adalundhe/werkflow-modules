from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2TransitGatewayNatRule(BaseModel):
    RuleNumber: StrictInt | None = None
    MatchSourceCidr: StrictStr | None = None
    NatCidr: StrictStr | None = None
    State: StrictStr | None = None
