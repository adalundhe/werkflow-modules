from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_journey_response import PinpointJourneyResponse


class PinpointDeleteJourneyResponse(BaseModel):
    JourneyResponse: PinpointJourneyResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
