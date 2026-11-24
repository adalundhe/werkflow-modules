from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EventBridgeDeleteRuleRequest(BaseModel):
    Name: StrictStr
    EventBusName: StrictStr | None = None
    Force: StrictBool | None = None
