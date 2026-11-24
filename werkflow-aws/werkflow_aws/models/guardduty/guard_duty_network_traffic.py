from __future__ import annotations
from pydantic import BaseModel, StrictInt


class GuardDutyNetworkTraffic(BaseModel):
    BytesSent: StrictInt | None = None
    BytesReceived: StrictInt | None = None
