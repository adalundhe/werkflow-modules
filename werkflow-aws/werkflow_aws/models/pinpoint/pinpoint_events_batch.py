from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_event import PinpointEvent
from .pinpoint_public_endpoint import PinpointPublicEndpoint


class PinpointEventsBatch(BaseModel):
    Endpoint: PinpointPublicEndpoint
    Events: dict[StrictStr, PinpointEvent]
