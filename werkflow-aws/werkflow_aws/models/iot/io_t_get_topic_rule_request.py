from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTGetTopicRuleRequest(BaseModel):
    ruleName: StrictStr
