from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EventBridgeEnableRuleRequest(BaseModel):
    Name: StrictStr
    EventBusName: StrictStr | None = None
