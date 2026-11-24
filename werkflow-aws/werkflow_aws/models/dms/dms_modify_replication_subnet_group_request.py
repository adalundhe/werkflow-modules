from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSModifyReplicationSubnetGroupRequest(BaseModel):
    ReplicationSubnetGroupIdentifier: StrictStr
    SubnetIds: list[StrictStr]
    ReplicationSubnetGroupDescription: StrictStr | None = None
