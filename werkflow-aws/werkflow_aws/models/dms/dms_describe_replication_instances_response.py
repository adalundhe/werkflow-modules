from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_replication_instance import DMSReplicationInstance


class DMSDescribeReplicationInstancesResponse(BaseModel):
    Marker: StrictStr | None = None
    ReplicationInstances: list[DMSReplicationInstance] | None = None
    ResponseMetadata: dict[str, Any] | None = None
