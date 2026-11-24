from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectRateLimiterStatus(BaseModel):
    maxAllowed: StrictInt | None = None
    inUse: StrictInt | None = None
    remaining: StrictInt | None = None
    totalBandwidth: StrictStr | None = None
