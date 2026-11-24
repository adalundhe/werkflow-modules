from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_segment_response import PinpointSegmentResponse


class PinpointDeleteSegmentResponse(BaseModel):
    SegmentResponse: PinpointSegmentResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
