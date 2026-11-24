from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudWatchAlarmPromQLCriteria(BaseModel):
    Query: StrictStr | None = None
    PendingPeriod: StrictInt | None = None
    RecoveryPeriod: StrictInt | None = None
