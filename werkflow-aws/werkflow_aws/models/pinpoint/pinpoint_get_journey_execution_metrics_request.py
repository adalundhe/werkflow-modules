from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetJourneyExecutionMetricsRequest(BaseModel):
    ApplicationId: StrictStr
    JourneyId: StrictStr
    NextToken: StrictStr | None = None
    PageSize: StrictStr | None = None
