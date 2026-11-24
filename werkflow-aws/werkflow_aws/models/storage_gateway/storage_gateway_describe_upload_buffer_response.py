from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayDescribeUploadBufferResponse(BaseModel):
    GatewayARN: StrictStr | None = None
    DiskIds: list[StrictStr] | None = None
    UploadBufferUsedInBytes: StrictInt | None = None
    UploadBufferAllocatedInBytes: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
