from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_segment_dimensions import PinpointSegmentDimensions
from .pinpoint_segment_reference import PinpointSegmentReference


class PinpointSegmentGroup(BaseModel):
    Dimensions: list[PinpointSegmentDimensions] | None = None
    SourceSegments: list[PinpointSegmentReference] | None = None
    SourceType: StrictStr | None = None
    Type: StrictStr | None = None
