from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_replication_subnet_group import DMSReplicationSubnetGroup


class DMSModifyReplicationSubnetGroupResponse(BaseModel):
    ReplicationSubnetGroup: DMSReplicationSubnetGroup | None = None
    ResponseMetadata: dict[str, Any] | None = None
