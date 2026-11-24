from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2PerformanceStatusSummary(BaseModel):
    Status: StrictStr | None = None
    ImpairedSince: datetime.datetime | StrictStr | None = None
    Remediation: StrictStr | None = None
