from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_replication_subnet_group import DMSReplicationSubnetGroup


class DMSDescribeReplicationSubnetGroupsResponse(BaseModel):
    Marker: StrictStr | None = None
    ReplicationSubnetGroups: list[DMSReplicationSubnetGroup] | None = None
    ResponseMetadata: dict[str, Any] | None = None
