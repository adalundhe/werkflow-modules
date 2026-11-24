from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_write_journey_request import PinpointWriteJourneyRequest


class PinpointUpdateJourneyRequest(BaseModel):
    ApplicationId: StrictStr
    JourneyId: StrictStr
    WriteJourneyRequest: PinpointWriteJourneyRequest
