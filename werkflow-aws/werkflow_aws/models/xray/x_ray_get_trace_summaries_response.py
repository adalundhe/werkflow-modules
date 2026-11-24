from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .x_ray_trace_summary import XRayTraceSummary


class XRayGetTraceSummariesResponse(BaseModel):
    TraceSummaries: list[XRayTraceSummary] | None = None
    ApproximateTime: datetime.datetime | StrictStr | None = None
    TracesProcessedCount: StrictInt | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
