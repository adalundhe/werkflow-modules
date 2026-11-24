from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_segments_response import PinpointSegmentsResponse


class PinpointGetSegmentVersionsResponse(BaseModel):
    SegmentsResponse: PinpointSegmentsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
