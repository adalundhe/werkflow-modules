from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DMSOrderableReplicationInstance(BaseModel):
    EngineVersion: StrictStr | None = None
    ReplicationInstanceClass: StrictStr | None = None
    StorageType: StrictStr | None = None
    MinAllocatedStorage: StrictInt | None = None
    MaxAllocatedStorage: StrictInt | None = None
    DefaultAllocatedStorage: StrictInt | None = None
    IncludedAllocatedStorage: StrictInt | None = None
    AvailabilityZones: list[StrictStr] | None = None
    ReleaseStatus: StrictStr | None = None
