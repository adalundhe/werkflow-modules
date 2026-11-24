from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTDeleteTopicRuleDestinationRequest(BaseModel):
    arn: StrictStr
