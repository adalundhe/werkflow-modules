from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayUpdateBandwidthRateLimitRequest(BaseModel):
    GatewayARN: StrictStr
    AverageUploadRateLimitInBitsPerSec: StrictInt | None = None
    AverageDownloadRateLimitInBitsPerSec: StrictInt | None = None
