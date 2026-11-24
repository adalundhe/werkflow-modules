from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_event_summary import DataZoneEventSummary


class DataZoneLineageEventSummary(BaseModel):
    id: StrictStr | None = None
    domainId: StrictStr | None = None
    processingStatus: StrictStr | None = None
    eventTime: datetime.datetime | StrictStr | None = None
    eventSummary: DataZoneEventSummary | None = None
    createdBy: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
