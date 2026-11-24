from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSMoveReplicationTaskRequest(BaseModel):
    ReplicationTaskArn: StrictStr
    TargetReplicationInstanceArn: StrictStr
