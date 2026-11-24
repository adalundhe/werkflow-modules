from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_item_response import PinpointItemResponse


class PinpointEventsResponse(BaseModel):
    Results: dict[StrictStr, PinpointItemResponse] | None = None
