from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ComputeOptimizerAccountEnrollmentStatus(BaseModel):
    accountId: StrictStr | None = None
    status: StrictStr | None = None
    statusReason: StrictStr | None = None
    lastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
