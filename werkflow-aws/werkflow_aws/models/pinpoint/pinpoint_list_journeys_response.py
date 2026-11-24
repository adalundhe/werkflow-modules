from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_journeys_response import PinpointJourneysResponse


class PinpointListJourneysResponse(BaseModel):
    JourneysResponse: PinpointJourneysResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
