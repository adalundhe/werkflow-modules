from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_event_dimensions import PinpointEventDimensions


class PinpointEventFilter(BaseModel):
    Dimensions: PinpointEventDimensions | None = None
    FilterType: StrictStr | None = None
