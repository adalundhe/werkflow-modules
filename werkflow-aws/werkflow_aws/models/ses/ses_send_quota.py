from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class SESSendQuota(BaseModel):
    Max24HourSend: StrictFloat | StrictInt | None = None
    MaxSendRate: StrictFloat | StrictInt | None = None
    SentLast24Hours: StrictFloat | StrictInt | None = None
