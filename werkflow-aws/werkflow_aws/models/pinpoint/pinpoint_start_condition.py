from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_event_start_condition import PinpointEventStartCondition
from .pinpoint_segment_condition import PinpointSegmentCondition


class PinpointStartCondition(BaseModel):
    Description: StrictStr | None = None
    EventStartCondition: PinpointEventStartCondition | None = None
    SegmentStartCondition: PinpointSegmentCondition | None = None
