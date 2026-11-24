from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDeleteReplicationSubnetGroupRequest(BaseModel):
    ReplicationSubnetGroupIdentifier: StrictStr
