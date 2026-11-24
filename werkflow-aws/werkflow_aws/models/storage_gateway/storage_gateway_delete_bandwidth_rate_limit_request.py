from __future__ import annotations
from pydantic import BaseModel, StrictStr


class StorageGatewayDeleteBandwidthRateLimitRequest(BaseModel):
    GatewayARN: StrictStr
    BandwidthType: StrictStr
