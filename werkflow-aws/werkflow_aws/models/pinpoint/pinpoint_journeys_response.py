from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_journey_response import PinpointJourneyResponse


class PinpointJourneysResponse(BaseModel):
    Item: list[PinpointJourneyResponse] | None = None
    NextToken: StrictStr | None = None
