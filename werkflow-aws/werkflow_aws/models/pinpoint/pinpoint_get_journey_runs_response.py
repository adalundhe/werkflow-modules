from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_journey_runs_response import PinpointJourneyRunsResponse


class PinpointGetJourneyRunsResponse(BaseModel):
    JourneyRunsResponse: PinpointJourneyRunsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
