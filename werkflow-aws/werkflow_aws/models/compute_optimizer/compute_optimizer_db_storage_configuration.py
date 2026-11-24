from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ComputeOptimizerDBStorageConfiguration(BaseModel):
    storageType: StrictStr | None = None
    allocatedStorage: StrictInt | None = None
    iops: StrictInt | None = None
    maxAllocatedStorage: StrictInt | None = None
    storageThroughput: StrictInt | None = None
