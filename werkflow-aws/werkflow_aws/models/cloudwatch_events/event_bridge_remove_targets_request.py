from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EventBridgeRemoveTargetsRequest(BaseModel):
    Rule: StrictStr
    Ids: list[StrictStr]
    EventBusName: StrictStr | None = None
    Force: StrictBool | None = None
