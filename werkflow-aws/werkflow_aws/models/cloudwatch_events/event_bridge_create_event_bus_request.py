from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .event_bridge_dead_letter_config import EventBridgeDeadLetterConfig
from .event_bridge_log_config import EventBridgeLogConfig
from .event_bridge_tag import EventBridgeTag


class EventBridgeCreateEventBusRequest(BaseModel):
    Name: StrictStr
    EventSourceName: StrictStr | None = None
    Description: StrictStr | None = None
    KmsKeyIdentifier: StrictStr | None = None
    DeadLetterConfig: EventBridgeDeadLetterConfig | None = None
    LogConfig: EventBridgeLogConfig | None = None
    Tags: list[EventBridgeTag] | None = None
