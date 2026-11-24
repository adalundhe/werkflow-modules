from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDeleteReplicationInstanceRequest(BaseModel):
    ReplicationInstanceArn: StrictStr
