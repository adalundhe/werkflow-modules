from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_trigger_source import DataZoneTriggerSource


class DataZoneNotebookRunSummary(BaseModel):
    id: StrictStr | None = None
    domainId: StrictStr | None = None
    owningProjectId: StrictStr | None = None
    notebookId: StrictStr | None = None
    scheduleId: StrictStr | None = None
    status: StrictStr | None = None
    triggerSource: DataZoneTriggerSource | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    createdBy: StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    updatedBy: StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    completedAt: datetime.datetime | StrictStr | None = None
