from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_violation_event import IoTViolationEvent


class IoTListViolationEventsResponse(BaseModel):
    violationEvents: list[IoTViolationEvent] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
