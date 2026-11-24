from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetJourneyRunsRequest(BaseModel):
    ApplicationId: StrictStr
    JourneyId: StrictStr
    PageSize: StrictStr | None = None
    Token: StrictStr | None = None
