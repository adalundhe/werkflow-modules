from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class StorageGatewayDisk(BaseModel):
    DiskId: StrictStr | None = None
    DiskPath: StrictStr | None = None
    DiskNode: StrictStr | None = None
    DiskStatus: StrictStr | None = None
    DiskSizeInBytes: StrictInt | None = None
    DiskAllocationType: StrictStr | None = None
    DiskAllocationResource: StrictStr | None = None
    DiskAttributeList: list[StrictStr] | None = None
