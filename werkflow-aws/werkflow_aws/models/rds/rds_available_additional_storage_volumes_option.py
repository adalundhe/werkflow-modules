from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class RDSAvailableAdditionalStorageVolumesOption(BaseModel):
    SupportsStorageAutoscaling: StrictBool | None = None
    SupportsStorageThroughput: StrictBool | None = None
    SupportsIops: StrictBool | None = None
    StorageType: StrictStr | None = None
    MinStorageSize: StrictInt | None = None
    MaxStorageSize: StrictInt | None = None
    MinIops: StrictInt | None = None
    MaxIops: StrictInt | None = None
    MinIopsPerGib: StrictFloat | StrictInt | None = None
    MaxIopsPerGib: StrictFloat | StrictInt | None = None
    MinStorageThroughput: StrictInt | None = None
    MaxStorageThroughput: StrictInt | None = None
