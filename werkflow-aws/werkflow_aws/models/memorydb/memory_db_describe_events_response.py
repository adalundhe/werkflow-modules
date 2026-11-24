from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_event import MemoryDBEvent


class MemoryDBDescribeEventsResponse(BaseModel):
    NextToken: StrictStr | None = None
    Events: list[MemoryDBEvent] | None = None
    ResponseMetadata: dict[str, Any] | None = None
