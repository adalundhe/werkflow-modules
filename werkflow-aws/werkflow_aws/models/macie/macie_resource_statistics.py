from __future__ import annotations
from pydantic import BaseModel, StrictInt


class MacieResourceStatistics(BaseModel):
    totalBytesClassified: StrictInt | None = None
    totalDetections: StrictInt | None = None
    totalDetectionsSuppressed: StrictInt | None = None
    totalItemsClassified: StrictInt | None = None
    totalItemsSensitive: StrictInt | None = None
    totalItemsSkipped: StrictInt | None = None
    totalItemsSkippedInvalidEncryption: StrictInt | None = None
    totalItemsSkippedInvalidKms: StrictInt | None = None
    totalItemsSkippedPermissionDenied: StrictInt | None = None
