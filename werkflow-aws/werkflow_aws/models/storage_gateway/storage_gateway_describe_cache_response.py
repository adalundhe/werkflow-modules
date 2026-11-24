from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class StorageGatewayDescribeCacheResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    DiskIds: list[StrictStr] | None = None
    CacheAllocatedInBytes: StrictInt | None = None
    CacheUsedPercentage: StrictFloat | StrictInt | None = None
    CacheDirtyPercentage: StrictFloat | StrictInt | None = None
    CacheHitPercentage: StrictFloat | StrictInt | None = None
    CacheMissPercentage: StrictFloat | StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
