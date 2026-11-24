from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayDescribeWorkingStorageResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    DiskIds: list[StrictStr] | None = None
    WorkingStorageUsedInBytes: StrictInt | None = None
    WorkingStorageAllocatedInBytes: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
