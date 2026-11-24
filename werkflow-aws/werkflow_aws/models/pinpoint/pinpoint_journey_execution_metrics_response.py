from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointJourneyExecutionMetricsResponse(BaseModel):
    ApplicationId: StrictStr | None = None
    JourneyId: StrictStr | None = None
    LastEvaluatedTime: StrictStr | None = None
    Metrics: dict[StrictStr, StrictStr] | None = None
