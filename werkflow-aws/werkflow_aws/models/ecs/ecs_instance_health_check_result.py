from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSInstanceHealthCheckResult(BaseModel):
    type: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    lastUpdated: datetime.datetime | StrictStr | None = None
    lastStatusChange: datetime.datetime | StrictStr | None = None
