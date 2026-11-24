from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointDeleteJourneyRequest(BaseModel):
    ApplicationId: StrictStr
    JourneyId: StrictStr
