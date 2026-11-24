from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_replication_instance_task_log import DMSReplicationInstanceTaskLog


class DMSDescribeReplicationInstanceTaskLogsResponse(BaseModel):
    ReplicationInstanceArn: StrictStr | None = None
    ReplicationInstanceTaskLogs: list[DMSReplicationInstanceTaskLog] | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
