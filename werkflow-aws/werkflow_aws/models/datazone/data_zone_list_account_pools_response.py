from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_account_pool_summary import DataZoneAccountPoolSummary


class DataZoneListAccountPoolsResponse(BaseModel):
    items: list[DataZoneAccountPoolSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
