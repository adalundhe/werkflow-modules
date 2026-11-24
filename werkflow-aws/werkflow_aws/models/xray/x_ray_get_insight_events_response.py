from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .x_ray_insight_event import XRayInsightEvent


class XRayGetInsightEventsResponse(BaseModel):
    InsightEvents: list[XRayInsightEvent] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
