from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_trace import XRayTrace


class XRayBatchGetTracesResponse(BaseModel):
    Traces: list[XRayTrace] | None = None
    UnprocessedTraceIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
