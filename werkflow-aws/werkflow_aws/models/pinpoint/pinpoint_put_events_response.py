from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_events_response import PinpointEventsResponse


class PinpointPutEventsResponse(BaseModel):
    EventsResponse: PinpointEventsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
