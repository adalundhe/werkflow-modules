from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTEnableTopicRuleRequest(BaseModel):
    ruleName: StrictStr
