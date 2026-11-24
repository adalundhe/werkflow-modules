from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class Route53ARCGatingRuleUpdate(BaseModel):
    Name: StrictStr
    SafetyRuleArn: StrictStr
    WaitPeriodMs: StrictInt
