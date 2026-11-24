from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EKSClientStat(BaseModel):
    userAgent: StrictStr | None = None
    numberOfRequestsLast30Days: StrictInt | None = None
    lastRequestTime: datetime.datetime | StrictStr | None = None
