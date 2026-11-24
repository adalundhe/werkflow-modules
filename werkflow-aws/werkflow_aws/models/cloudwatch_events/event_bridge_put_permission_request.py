from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .event_bridge_condition import EventBridgeCondition


class EventBridgePutPermissionRequest(BaseModel):
    EventBusName: StrictStr | None = None
    Action: StrictStr | None = None
    Principal: StrictStr | None = None
    StatementId: StrictStr | None = None
    Condition: EventBridgeCondition | None = None
    Policy: StrictStr | None = None
