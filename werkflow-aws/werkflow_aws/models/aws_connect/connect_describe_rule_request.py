from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDescribeRuleRequest(BaseModel):
    InstanceId: StrictStr
    RuleId: StrictStr
