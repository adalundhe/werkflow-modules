from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_journey_run_response import PinpointJourneyRunResponse


class PinpointJourneyRunsResponse(BaseModel):
    Item: list[PinpointJourneyRunResponse] | None = None
    NextToken: StrictStr | None = None
