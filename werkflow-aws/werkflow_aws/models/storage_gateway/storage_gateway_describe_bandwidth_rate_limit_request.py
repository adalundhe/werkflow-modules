from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDescribeBandwidthRateLimitRequest(BaseModel):
    GatewayARN: StrictStr
