from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .x_ray_unprocessed_trace_segment import XRayUnprocessedTraceSegment


class XRayPutTraceSegmentsResponse(BaseModel):
    UnprocessedTraceSegments: list[XRayUnprocessedTraceSegment] | None = None
    ResponseMetadata: dict[str, Any] | None = None
