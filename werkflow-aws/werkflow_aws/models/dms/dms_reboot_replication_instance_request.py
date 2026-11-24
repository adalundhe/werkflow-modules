from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DMSRebootReplicationInstanceRequest(BaseModel):
    ReplicationInstanceArn: StrictStr
    ForceFailover: StrictBool | None = None
    ForcePlannedFailover: StrictBool | None = None
