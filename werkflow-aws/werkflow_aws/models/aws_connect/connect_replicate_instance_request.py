from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectReplicateInstanceRequest(BaseModel):
    InstanceId: StrictStr
    ReplicaRegion: StrictStr
    ClientToken: StrictStr | None = None
    ReplicaAlias: StrictStr | None = None
