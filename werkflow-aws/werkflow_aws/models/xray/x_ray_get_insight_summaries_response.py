from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_insight_summary import XRayInsightSummary


class XRayGetInsightSummariesResponse(BaseModel):
    InsightSummaries: list[XRayInsightSummary] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
