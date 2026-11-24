from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_events_request import PinpointEventsRequest


class PinpointPutEventsRequest(BaseModel):
    ApplicationId: StrictStr
    EventsRequest: PinpointEventsRequest
