from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RDSAdditionalStorageVolume(BaseModel):
    VolumeName: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    IOPS: StrictInt | None = None
    MaxAllocatedStorage: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    StorageType: StrictStr | None = None
