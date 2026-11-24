from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class RDSAdditionalStorageVolumeOutputModel(BaseModel):
    VolumeName: StrictStr | None = None
    StorageVolumeStatus: StrictStr | None = None
    StorageOperationStatus: StrictStr | None = None
    StorageOperationPercentProgress: StrictInt | None = None
    AllocatedStorage: StrictInt | None = None
    IOPS: StrictInt | None = None
    MaxAllocatedStorage: StrictInt | None = None
    StorageThroughput: StrictInt | None = None
    StorageType: StrictStr | None = None
