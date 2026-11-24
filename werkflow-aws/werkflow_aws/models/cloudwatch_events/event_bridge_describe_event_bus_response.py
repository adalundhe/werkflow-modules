from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .event_bridge_dead_letter_config import EventBridgeDeadLetterConfig
from .event_bridge_log_config import EventBridgeLogConfig


class EventBridgeDescribeEventBusResponse(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    Description: StrictStr | None = None
    KmsKeyIdentifier: StrictStr | None = None
    DeadLetterConfig: EventBridgeDeadLetterConfig | None = None
    Policy: StrictStr | None = None
    LogConfig: EventBridgeLogConfig | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ManagedBy: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
