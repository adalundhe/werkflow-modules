from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DevOpsGuruAnomalyReportedTimeRange(BaseModel):
    OpenTime: datetime.datetime | StrictStr | None = None
    CloseTime: datetime.datetime | StrictStr | None = None
