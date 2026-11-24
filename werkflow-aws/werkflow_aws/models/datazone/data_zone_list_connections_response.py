from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_connection_summary import DataZoneConnectionSummary


class DataZoneListConnectionsResponse(BaseModel):
    items: list[DataZoneConnectionSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
