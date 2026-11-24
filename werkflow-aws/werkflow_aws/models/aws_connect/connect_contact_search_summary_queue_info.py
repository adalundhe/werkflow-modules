from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectContactSearchSummaryQueueInfo(BaseModel):
    Id: StrictStr | None = None
    EnqueueTimestamp: datetime.datetime | StrictStr | None = None
