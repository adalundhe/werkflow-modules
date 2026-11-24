from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_endpoint_item_response import PinpointEndpointItemResponse
from .pinpoint_event_item_response import PinpointEventItemResponse


class PinpointItemResponse(BaseModel):
    EndpointItemResponse: PinpointEndpointItemResponse | None = None
    EventsItemResponse: dict[StrictStr, PinpointEventItemResponse] | None = None
