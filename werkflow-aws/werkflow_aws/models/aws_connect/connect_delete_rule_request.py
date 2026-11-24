from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectDeleteRuleRequest(BaseModel):
    InstanceId: StrictStr
    RuleId: StrictStr
