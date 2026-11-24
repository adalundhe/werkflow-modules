from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .memory_db_service_update import MemoryDBServiceUpdate


class MemoryDBDescribeServiceUpdatesResponse(BaseModel):
    NextToken: StrictStr | None = None
    ServiceUpdates: list[MemoryDBServiceUpdate] | None = None
    ResponseMetadata: dict[str, Any] | None = None
