from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeDescribeRuleRequest(BaseModel):
    Name: StrictStr
    EventBusName: StrictStr | None = None
