from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_event import DMSEvent


class DMSDescribeEventsResponse(BaseModel):
    Marker: StrictStr | None = None
    Events: list[DMSEvent] | None = None
    ResponseMetadata: dict[str, Any] | None = None
