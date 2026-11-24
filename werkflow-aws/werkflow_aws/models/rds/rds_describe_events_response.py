from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .rds_event import RDSEvent


class RDSDescribeEventsResponse(BaseModel):
    Marker: StrictStr | None = None
    Events: list[RDSEvent] | None = None
    ResponseMetadata: dict[str, Any] | None = None
