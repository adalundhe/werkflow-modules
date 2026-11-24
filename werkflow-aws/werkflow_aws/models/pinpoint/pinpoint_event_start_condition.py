from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_event_filter import PinpointEventFilter


class PinpointEventStartCondition(BaseModel):
    EventFilter: PinpointEventFilter | None = None
    SegmentId: StrictStr | None = None
