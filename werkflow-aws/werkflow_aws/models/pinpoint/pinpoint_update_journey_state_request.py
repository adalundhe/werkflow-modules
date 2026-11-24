from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_journey_state_request import PinpointJourneyStateRequest


class PinpointUpdateJourneyStateRequest(BaseModel):
    ApplicationId: StrictStr
    JourneyId: StrictStr
    JourneyStateRequest: PinpointJourneyStateRequest
