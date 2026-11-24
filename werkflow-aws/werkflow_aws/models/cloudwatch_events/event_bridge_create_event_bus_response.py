from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_dead_letter_config import EventBridgeDeadLetterConfig
from .event_bridge_log_config import EventBridgeLogConfig


class EventBridgeCreateEventBusResponse(BaseModel):
    EventBusArn: StrictStr | None = None
    Description: StrictStr | None = None
    KmsKeyIdentifier: StrictStr | None = None
    DeadLetterConfig: EventBridgeDeadLetterConfig | None = None
    LogConfig: EventBridgeLogConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
