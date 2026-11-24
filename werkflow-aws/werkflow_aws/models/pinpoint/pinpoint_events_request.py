from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_events_batch import PinpointEventsBatch


class PinpointEventsRequest(BaseModel):
    BatchItem: dict[StrictStr, PinpointEventsBatch]
