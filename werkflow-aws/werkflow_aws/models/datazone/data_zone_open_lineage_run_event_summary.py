from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_name_identifier import DataZoneNameIdentifier


class DataZoneOpenLineageRunEventSummary(BaseModel):
    eventType: StrictStr | None = None
    runId: StrictStr | None = None
    job: DataZoneNameIdentifier | None = None
    inputs: list[DataZoneNameIdentifier] | None = None
    outputs: list[DataZoneNameIdentifier] | None = None
