from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_event_stream import PinpointEventStream


class PinpointGetEventStreamResponse(BaseModel):
    EventStream: PinpointEventStream | None = None
    ResponseMetadata: dict[str, Any] | None = None
