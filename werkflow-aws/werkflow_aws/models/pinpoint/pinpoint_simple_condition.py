from __future__ import annotations
from pydantic import BaseModel
from .pinpoint_event_condition import PinpointEventCondition
from .pinpoint_segment_condition import PinpointSegmentCondition
from .pinpoint_segment_dimensions import PinpointSegmentDimensions


class PinpointSimpleCondition(BaseModel):
    EventCondition: PinpointEventCondition | None = None
    SegmentCondition: PinpointSegmentCondition | None = None
    SegmentDimensions: PinpointSegmentDimensions | None = None
