from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetJourneyRunExecutionActivityMetricsRequest(BaseModel):
    ApplicationId: StrictStr
    JourneyActivityId: StrictStr
    JourneyId: StrictStr
    RunId: StrictStr
    NextToken: StrictStr | None = None
    PageSize: StrictStr | None = None
