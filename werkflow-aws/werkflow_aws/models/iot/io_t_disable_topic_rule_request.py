from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDisableTopicRuleRequest(BaseModel):
    ruleName: StrictStr
