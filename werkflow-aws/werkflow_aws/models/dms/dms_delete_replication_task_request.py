from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDeleteReplicationTaskRequest(BaseModel):
    ReplicationTaskArn: StrictStr
