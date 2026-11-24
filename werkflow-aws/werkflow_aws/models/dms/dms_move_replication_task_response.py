from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_replication_task import DMSReplicationTask


class DMSMoveReplicationTaskResponse(BaseModel):
    ReplicationTask: DMSReplicationTask | None = None
    ResponseMetadata: dict[str, Any] | None = None
