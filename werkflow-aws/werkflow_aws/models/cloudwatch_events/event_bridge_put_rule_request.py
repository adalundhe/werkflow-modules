from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .event_bridge_tag import EventBridgeTag


class EventBridgePutRuleRequest(BaseModel):
    Name: StrictStr
    ScheduleExpression: StrictStr | None = None
    EventPattern: StrictStr | None = None
    State: Literal['ENABLED', 'DISABLED', 'ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS'] | None = None
    Description: StrictStr | None = None
    RoleArn: StrictStr | None = None
    Tags: list[EventBridgeTag] | None = None
    EventBusName: StrictStr | None = None
