from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CloudTrailListInsightsMetricDataResponse(BaseModel):
    TrailARN: StrictStr | None = None
    EventSource: StrictStr | None = None
    EventName: StrictStr | None = None
    InsightType: StrictStr | None = None
    ErrorCode: StrictStr | None = None
    Timestamps: list[datetime.datetime | StrictStr] | None = None
    Values: list[StrictFloat | StrictInt] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
