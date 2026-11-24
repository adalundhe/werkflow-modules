from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_zone_lineage_event_summary import DataZoneLineageEventSummary


class DataZoneListLineageEventsResponse(BaseModel):
    items: list[DataZoneLineageEventSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
