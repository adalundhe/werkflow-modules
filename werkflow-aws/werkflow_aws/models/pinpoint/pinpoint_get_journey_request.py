from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointGetJourneyRequest(BaseModel):
    ApplicationId: StrictStr
    JourneyId: StrictStr
