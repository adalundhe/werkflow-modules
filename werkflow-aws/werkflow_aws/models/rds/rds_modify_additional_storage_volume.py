from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class RDSModifyAdditionalStorageVolume(BaseModel):
    VolumeName: StrictStr
    AllocatedStorage: StrictInt | None = None
    IOPS: StrictInt | None = None
    MaxAllocatedStorage: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    StorageType: StrictStr | None = None
    SetForDelete: StrictBool | None = None
