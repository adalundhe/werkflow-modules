from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_replication_task import DMSReplicationTask


class DMSDescribeReplicationTasksResponse(BaseModel):
    Marker: StrictStr | None = None
    ReplicationTasks: list[DMSReplicationTask] | None = None
    ResponseMetadata: dict[str, Any] | None = None
