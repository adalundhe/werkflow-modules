from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NetworkManagerNatRuleRequest(BaseModel):
    RuleNumber: StrictInt
    MatchSourceCidr: StrictStr
    NatCidr: StrictStr
