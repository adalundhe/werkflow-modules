from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointJourneyRunExecutionActivityMetricsResponse(BaseModel):
    ActivityType: StrictStr | None = None
    ApplicationId: StrictStr | None = None
    JourneyActivityId: StrictStr | None = None
    JourneyId: StrictStr | None = None
    LastEvaluatedTime: StrictStr | None = None
    Metrics: dict[StrictStr, StrictStr] | None = None
    RunId: StrictStr | None = None
