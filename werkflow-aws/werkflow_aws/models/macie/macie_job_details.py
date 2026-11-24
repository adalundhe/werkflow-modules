from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class MacieJobDetails(BaseModel):
    isDefinedInJob: StrictStr | None = None
    isMonitoredByJob: StrictStr | None = None
    lastJobId: StrictStr | None = None
    lastJobRunTime: datetime.datetime | StrictStr | None = None
