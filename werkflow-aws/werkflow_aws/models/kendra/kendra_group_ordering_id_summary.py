from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class KendraGroupOrderingIdSummary(BaseModel):
    Status: StrictStr | None = None
    LastUpdatedAt: datetime.datetime | StrictStr | None = None
    ReceivedAt: datetime.datetime | StrictStr | None = None
    OrderingId: StrictInt | None = None
    FailureReason: StrictStr | None = None
