from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchResourceMetricSelection(BaseModel):
    IncludeMetrics: list[StrictStr] | None = None
