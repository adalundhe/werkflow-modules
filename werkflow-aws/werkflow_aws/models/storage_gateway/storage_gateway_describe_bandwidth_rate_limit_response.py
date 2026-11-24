from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayDescribeBandwidthRateLimitResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    AverageUploadRateLimitInBitsPerSec: StrictInt | None = None
    AverageDownloadRateLimitInBitsPerSec: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
