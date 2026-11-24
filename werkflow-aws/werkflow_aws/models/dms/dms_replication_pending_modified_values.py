from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class DMSReplicationPendingModifiedValues(BaseModel):
    ReplicationInstanceClass: StrictStr | None = None
    AllocatedStorage: StrictInt | None = None
    MultiAZ: StrictBool | None = None
    EngineVersion: StrictStr | None = None
    NetworkType: StrictStr | None = None
