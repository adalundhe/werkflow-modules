from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .neptune_event import NeptuneEvent


class NeptuneDescribeEventsResponse(BaseModel):
    Marker: StrictStr | None = None
    Events: list[NeptuneEvent] | None = None
    ResponseMetadata: dict[str, Any] | None = None
