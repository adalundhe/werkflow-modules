from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_segment_dimensions import PinpointSegmentDimensions
from .pinpoint_segment_group_list import PinpointSegmentGroupList


class PinpointWriteSegmentRequest(BaseModel):
    Dimensions: PinpointSegmentDimensions | None = None
    Name: StrictStr | None = None
    SegmentGroups: PinpointSegmentGroupList | None = None
    tags: dict[StrictStr, StrictStr] | None = None
