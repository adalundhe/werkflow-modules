from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetJourneyExecutionActivityMetricsRequest(BaseModel):
    ApplicationId: StrictStr
    JourneyActivityId: StrictStr
    JourneyId: StrictStr
    NextToken: StrictStr | None = None
    PageSize: StrictStr | None = None
