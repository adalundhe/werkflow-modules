from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_segment_response import PinpointSegmentResponse


class PinpointSegmentsResponse(BaseModel):
    Item: list[PinpointSegmentResponse] | None = None
    NextToken: StrictStr | None = None
