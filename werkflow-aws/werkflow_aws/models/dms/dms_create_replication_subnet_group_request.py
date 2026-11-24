from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dms_tag import DMSTag


class DMSCreateReplicationSubnetGroupRequest(BaseModel):
    ReplicationSubnetGroupIdentifier: StrictStr
    ReplicationSubnetGroupDescription: StrictStr
    SubnetIds: list[StrictStr]
    Tags: list[DMSTag] | None = None
