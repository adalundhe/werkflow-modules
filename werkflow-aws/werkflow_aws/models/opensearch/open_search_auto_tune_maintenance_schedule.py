from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .open_search_duration import OpenSearchDuration


class OpenSearchAutoTuneMaintenanceSchedule(BaseModel):
    StartAt: datetime.datetime | StrictStr | None = None
    Duration: OpenSearchDuration | None = None
    CronExpressionForRecurrence: StrictStr | None = None
