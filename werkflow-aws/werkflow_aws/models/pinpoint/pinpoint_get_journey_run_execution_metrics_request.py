from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetJourneyRunExecutionMetricsRequest(BaseModel):
    ApplicationId: StrictStr
    JourneyId: StrictStr
    RunId: StrictStr
    NextToken: StrictStr | None = None
    PageSize: StrictStr | None = None
