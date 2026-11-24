from __future__ import annotations
from pydantic import BaseModel
from .data_zone_open_lineage_run_event_summary import DataZoneOpenLineageRunEventSummary


class DataZoneEventSummary(BaseModel):
    openLineageRunEventSummary: DataZoneOpenLineageRunEventSummary | None = None
